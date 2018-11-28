#include <cstdio>
#include <fstream>
using namespace std;
int graph[100][100];
//int dir[16] = {-1,0,0,-1,-1,0,0,1,-1,0,0,-1,-1,0,0,1};
int main()
{
    ifstream input;
    input.open("C:\\Users\\Administrator\\Desktop\\B-large.in");
    int t;
    //cin>>t;
    input>>t;
    int n,m;
    ofstream output;
    output.open("C:\\Users\\Administrator\\Desktop\\B-large.out");
    for (int c = 1;c <= t;c++)
    {
        //cin>>n>>m;
        bool flag = true;
        input>>n>>m;
        for(int i = 0;i < n;i++)
            for(int j = 0;j < m;j++)
                input>>graph[i][j];
        for(int i = 0;i < n;i++)
        {
            if(flag)
            {
                for(int j = 0;j < m;j++)
                {
                    if(flag)
                    {
                        int x = i-1;
                        int y = j;
                        bool round1 = true;
                        bool round2 = true;
                        while(x >= 0 && round1)
                        {
                            if(graph[x][y] > graph[i][j])
                                round1 = false;
                            x--;
                        }
                        x = i+1;
                        while(round1 && x < n)
                        {

                            if(graph[x][y] > graph[i][j])
                                round1 = false;
                            x++;
                        }
                        if(!round1)
                        {
                            x = i;
                            y = j-1;
                            while(y>=0)
                            {
                                if(graph[x][y] > graph[i][j])
                                    round2 = false;
                                y--;
                            }
                            y = j+1;
                            while(round2 && y < m)
                            {
                                if(graph[x][y] > graph[i][j])
                                    round2 = false;
                                y++;
                            }
                        }
                        if(round1 == false && round2 == false)
                            flag = false;

                    }
                    else
                    break;
                }
            }
            else
            break;
        }
        if(flag)
        {
            //cout<<"Case #"<<c<<": YES\n";
            output<<"Case #"<<c<<": YES\n";
        }
        else
        {
            //cout<<"Case #"<<c<<": NO\n";
            output<<"Case #"<<c<<": NO\n";
        }

    }
    input.close();
    output.close();
}
