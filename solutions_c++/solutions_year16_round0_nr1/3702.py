#include <bits/stdc++.h>
using namespace std;
/*char line[200];
int main()
{
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        gets(line);
        int n = strlen(line);
        int cont = 1;
        for(int i = 0; i<n-1; i++)
        {
            if(line[i]!=line[i+1]) cont++;
        }
        int solution = 0;
        if(cont==1)
        {
            if(line[0]=='+') solution = 0;
            else solution = 1;
        }
        else
        {
            if(line[n-1]=='+') cont--;
            solution = cont;
        }
        printf("Case #%d: %d\n", t, solution);
    }
}*/
int main()
{
    int T;
    long long N;
    scanf("%d", &T);
    for(int t = 1; t<=T; t++)
    {
        scanf("%lld", &N);
        if(N==0) printf("Case #%d: INSOMNIA\n", t);
        else
        {
            bitset<10> visited;
            visited.reset();
            long long i = 1;
            while(true)
            {
                long long aux = i*N;
                while(aux!=0)
                {
                    visited[aux%10] = true;
                    aux/=10;
                }
                bool m_break = true;
                for(int j = 0; j<10 && m_break; j++) m_break = (m_break && visited[j]);
                if(m_break) break;
                i++;
            }
            printf("Case #%d: %lld\n", t, i*N);
        }
    }
}
