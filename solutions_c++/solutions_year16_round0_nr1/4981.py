#include<iostream>
#include<cstdio>

using namespace std;

int cs=1;

int main()
{
    FILE *in=freopen("al.in","r",stdin);
    FILE *out =freopen("Alarge.txt","w",stdout);

    int t;
    cin>>t;
    while(t--)
    {
        long long int n,a;
        bool seen[10]={false,false,false,false,false,false,false,false,false,false};

        cin>>n;
        a=n;
        if(a==0)
        {
            //Case #1: INSOMNIA
            cout<<"Case #"<<cs<<": INSOMNIA"<<endl;
            cs++;
        }
        else
        {
            long long int q=2;
           long long int y=a;

          while((seen[0]==false) || (seen[1]==false) || (seen[2]==false) || (seen[3]==false) || (seen[4]==false) || (seen[5]==false) || (seen[6]==false) || (seen[7]==false) || (seen[8]==false) || (seen[9]==false) )
          {

              y=a;
              while(a!=0)
              {
                  int v= a%10;
                  seen[v]=true;
                  a=a/10;
              }
             // a=y;
              a= q*n;
              q++;

          }

          cout<<"Case #"<<cs<<": "<<y<<endl;
            cs++;

        }

    }

   fclose(in);
   fclose(out);
    return 0;
}

