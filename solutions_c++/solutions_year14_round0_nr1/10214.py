# include<iostream>
# include<cstdio>
# include<fstream>
# include<sstream>
# define N 4
using namespace std;
int main()
{
    int t,a,b,i,j,k=1,c,x;
    int a1[N][N],b1[N][N];
    freopen("A-small-attempt0.in","r",stdin);
    cin>>t;
    cin.ignore();
    ofstream m;
    m.open("otp.txt");
    while(t--)
    {
              c=0;
              cin>>a;
              cin.ignore();
              for(i=0;i<N;++i)
              for(j=0;j<N;++j)
              cin>>a1[i][j];
              cin.ignore();
              cin>>b;
              cin.ignore();
              for(i=0;i<N;++i)
              for(j=0;j<N;++j)
              cin>>b1[i][j];
              cin.ignore();
              for(i=0;i<4;++i)
              {
                              for(j=0;j<4;++j)
                              {
                                              if(a1[a-1][i]==b1[b-1][j])
                                              {
                                                                        ++c;
                                                                        x=a1[a-1][i];
                                              }
                              }
              }
              m<<"Case #"<<k++<<": ";
              if(c==1)
              m<<x;
              else if(c==0)
              m<<"Volunteer cheated!";
              else
              m<<"Bad magician!";
              m<<endl;
    }
    m.close();
    return 0;
}
