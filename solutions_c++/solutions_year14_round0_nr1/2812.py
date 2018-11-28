#include<fstream>
using namespace std;
int main()
{
    int t,a[4],b[4],m,i,j,g,n,c=1;
    ifstream fin;
    ofstream fout;
    fin.open("abc.in");
    fout.open("out.out");
    fin>>t;
    while(t--)
    {
              n=0;
              fin>>m;
              for(i=0;i<4;i++)
              {
                  for(j=0;j<4;j++)
                  {
                      if(i==m-1)
                          fin>>a[j];
                      else
                          fin>>g;
                  }
              }
              fin>>m;
              for(i=0;i<4;i++)
              {
                  for(j=0;j<4;j++)
                  {
                      if(i==m-1)
                          fin>>b[j];
                      else
                          fin>>g;
                  }
              }
              for(i=0;i<4;i++)
              {
                  for(j=0;j<4;j++)
                  {
                      if(a[i]==b[j])
                      {
                          g=a[i];
                          n++;
                      }
                  }
              }
              if(n==0)
                  fout<<"Case #"<<c<<": Volunteer cheated!";
              else if(n==1)
                  fout<<"Case #"<<c<<": "<<g;
              else
                  fout<<"Case #"<<c<<": Bad magician!";
              fout<<endl;
              c++;
    }
    fin.close();
    fout.close();
    return 0;
}
                          
    
