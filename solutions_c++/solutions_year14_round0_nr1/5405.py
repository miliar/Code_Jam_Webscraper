/*N*/
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<iomanip>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<fstream>
#define N 1010

using namespace std;
//int a[N];
//int a[4][20]={0};
//int b[4][20]={0};
int main()
{
    int t; int test= 0;
    //ifstream fin("file.in");
    //ofstream oin("file.out");
    //FILE *p;    p= fopen("")
    cin>>t;
    while(t-- && t> -1)
    {
        int a[4][20]={0};
        int b[4][20]={0};
        test++;
        int x;
        scanf("%d",&x); x--;
        int temp;
        for(int i= 0;i< 4;i++)
        {
            for(int j= 0;j< 4;j++)
            {
                scanf("%d", &temp);
                a[i][temp]++;
            }
        }

        int y;
        scanf("%d", &y); y--;

        for(int i= 0;i< 4;i++)
        {
            for(int j= 0;j< 4;j++)
            {
                scanf("%d", &temp);
                b[i][temp]++;
            }
        }

        int COUNT= 0, sum=0;
        for(int i= 1;i<= 16;i++)
        {
            if(a[x][i]!= 0 && b[y][i]!= 0)
            {
                COUNT++;
                sum= i;
            }
        }
        //cout<<COUNT<<" -"<<sum<<endl;
        if(COUNT== 0)
        {
            cout<<"Case #"<<test<<": Volunteer cheated!\n";
        }
        else if(COUNT== 1)
        {
            cout<<"Case #"<<test<<": "<<sum<<endl;
        }
        else
        {
            cout<<"Case #"<<test<<": Bad magician!\n";
        }
    }

    return 0;
}
