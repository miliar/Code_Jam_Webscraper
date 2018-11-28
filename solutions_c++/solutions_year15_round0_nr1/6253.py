#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
    string line;
    int t;
    int i,n;
    ifstream file ("A-large.in");
    ofstream out;
    out.open("an1.txt");
    file>>t;
    //cout<<t<<endl;
    int l=t;
    while(t--)
    {
        file>>n;
    //cout<<n<<endl;
            //cout<<endl;
            char a[n+1];
            int b[n+1];
            for(i=0;i<=n;i++)
                file>>a[i];
            for(i=0;i<=n;i++)
            {
                b[i]=a[i]-'0';

            }
           /* for(i=0;i<=n;i++)
                cout<<b[i]<<"\t";
            cout<<endl;*/
            int count=0;
            int add=0;
            int sum=0;
            for(i=0;i<=n;i++)
            {
                if(count>=i)
                {count+=b[i];
                 //cout<<count<<" count"<<endl;


                }
                else
                {
                    add=i-count;
                    count=count+add+b[i];
                   // cout<<"add "<<add<<endl;
                }
                sum+=b[i];
               // cout<<sum<<" sum"<<endl;
            }
            //cout<<count<<" count"<<endl;
             //file.close();


            out<<"Case #"<<l-t<<": "<<count-sum<<endl;
           // cout<<"Case #"<<l-t<<": "<<add<<endl;
    }


}
