#include <bits/stdc++.h>
using namespace std;
/*char word[5000];
int main()
{
    list<char> m_list;
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        scanf(" %s", word);
        int n = strlen(word);
        m_list.clear();
        m_list.push_front(word[0]);
        for(int i = 1; i<n; i++)
        {
            if(word[i]>=m_list.front()) m_list.push_front(word[i]);
            else m_list.push_back(word[i]);
        }
        for(list<char>::iterator i = m_list.begin(); i!=m_list.end(); i++)
        {
            printf("%c", (*i));
        }
        printf("\n");
    }
}
*/

int N;
int data[100][100];
bitset<200> visited, row;
pair<int, int> idx[100];
int complete[100][100];



bool isComplete()
{
    for(int i = 0; i<N; i++)
    {
        for(int j = 0; j<N; j++)
        {
            if(complete[i][j]==-1) return false;
        }
    }
    return true;
}

void BFS(int k)
{
    if(isComplete()) return;
    if(k>=N-1) return;
    if(row[k]) BFS(k+1);
    else
    {
        int idx1 = idx[k].first;
        int idx2 = idx[k].second;

        bool posible = true;

        for(int i = 0; i<N && posible; i++)
        {
            if(complete[k][i]!=-1 && complete[k][i]!=data[idx1][i]) posible = false;
            if(complete[i][k]!=-1 && complete[i][k]!=data[idx2][i]) posible = false;
        }

        vector<int> markrow, markcol;

        if(posible)
        {
            for(int i = 0; i<N; i++)
            {
                if(complete[i][k]==-1)
                {
                    complete[i][k] = data[idx2][i];
                    markrow.push_back(i);
                }
                if(complete[k][i]==-1)
                {
                    complete[k][i] = data[idx1][i];
                    markcol.push_back(i);
                }
            }
            BFS(k+1);
        }
        if(isComplete()) return;
        else
        {
            /*for(int i = 0; i<(int)markcol.size(); i++) complete[k][markcol[i]] = -1;
            for(int i = 0; i<(int)markrow.size(); i++) complete[markrow[i]][k] = -1;*/

            for(int i = 0; i<N; i++)
            {
                complete[i][k] = data[idx1][i];
                complete[k][i] = data[idx2][i];
            }


        }
    }
}


int main()
{
    int T, idx_s, idx_new;
    scanf("%d", &T);
    for(int t = 1; t<=T; t++)
    {
        visited.reset();
        scanf("%d", &N);
        for(int i = 0; i<2*N-1; i++)
            for(int j = 0; j<N; j++)
                scanf("%d", &data[i][j]);
        for(int i = 0; i<N; i++)
        {
            priority_queue<pair<int, int> > m_q;
            for(int j = 0; j<2*N-1; j++)
            {
                if(!visited[j]) m_q.push(pair<int, int>(data[j][i], j));
                if((int)m_q.size()>2) m_q.pop();
            }
            if((int)m_q.size()<2)
            {
                idx_new = i;
                idx_s = (m_q.top()).second;
            }
            else
            {
                int idx1 = (m_q.top()).second;
                int val1 = (m_q.top()).first;
                m_q.pop();
                int idx2 = (m_q.top()).second;
                int val2 = (m_q.top()).first;
                m_q.pop();

                /*printf("idx = %d %d\n", idx1, idx2);
                getchar();*/

                if(val1!=val2)
                {
                    idx_new = i;
                    if(val1<val2) idx_s = idx1;
                    else idx_s = idx2;
                    visited[idx_s] = true;
                }
                else
                {
                    visited[idx1] = true;
                    visited[idx2] = true;

                    idx[i] = pair<int, int> (idx1, idx2);
                }
            }
        }
        for(int i = 0; i<N; i++)
        {
            if(i!=idx_new)
            {
                int idx1 = idx[i].first;
                int idx2 = idx[i].second;


                if(data[idx1][idx_new]==data[idx_s][i]) data[2*N-1][i] = data[idx2][idx_new];
                if(data[idx2][idx_new]==data[idx_s][i]) data[2*N-1][i] = data[idx1][idx_new];
            }
            else
            {
                data[2*N-1][idx_new] = data[idx_s][idx_new];
                idx[idx_new] = pair<int, int> (idx_s, 2*N-1);
            }
        }

        printf("Case #%d: ", t);
        for(int i = 0; i<N; i++) printf(" %d", data[2*N - 1][i]);
        printf("\n");
        /*for(int i = 0; i<N; i++)
            for(int j = 0; j<N; j++) complete[i][j] = -1;
        for(int i = 0; i<N; i++)
        {
            complete[idx_new][i] = data[2*N - 1][i];
            complete[i][idx_new] = data[idx_s][i];
        }



        row.reset();
        for(int i = 0; i<N; i++)
        {
            int idx1 = idx[i].first;
            int idx2 = idx[i].second;

            complete[i][i] = data[idx1][i];


            if(data[idx1][idx_new]!=data[idx2][idx_new])
            {
                row[i] = true;
                if(data[idx1][idx_new]==complete[i][idx_new])
                {
                    for(int j = 0; j<N; j++)
                    {
                        complete[i][j] = data[idx1][j];
                        complete[j][i] = data[idx2][j];
                    }
                }
                else
                {
                    for(int j = 0; j<N; j++)
                    {
                        complete[i][j] = data[idx2][j];
                        complete[j][i] = data[idx1][j];
                    }
                }
            }
        }*/
    }
}
