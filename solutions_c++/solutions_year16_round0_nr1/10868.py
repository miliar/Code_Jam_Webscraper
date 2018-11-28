#include <bits/stdc++.h>
#include <fstream>
#define in  unsigned long long int
bool p[15];



using namespace std;

in a,b,c,t;

int main()
{   memset(p,false,sizeof(p));
     //freopen("A-small-attempt0.in","r",stdin);
     ifstream infile;
     infile.open("A-large.in");
     //freopen("output_file_name.out","w",stdout);
      ofstream outfile;
   outfile.open("output_file_name.out");


    infile>>t;
    for(int d=1; d<=t; d++)
    {infile>>a;
     in k=0;
    if(a==0)
          {
              outfile<<"Case #"<<d<<": INSOMNIA"<<endl;

              continue;
          }
    in i=1;

    in flag=0;
    for(int i=1; i; i++)
    {
        c=b=a*i;

        while(b/10!=0)
        {
            p[b%10]=true;
            b=b/10;
        }
        p[b]=true;
        //cout<<"b "<<b<<endl;

            int j;
        for( j=k; j<=10; j++)
        {
            if(p[j]==false)
                break;

                //cout<<j<<" "<<p[j]<<endl;
        }
          k=j;
        if(k<10)
            continue;
        else

        {outfile<<"Case #"<<d<<": "<<c<<endl;
          break;
        }



    }memset(p,false,sizeof(p));

    }
}

