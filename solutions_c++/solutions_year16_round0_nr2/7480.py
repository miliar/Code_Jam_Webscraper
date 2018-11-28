#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    char s[101],c;
    int t,i,j,k,l,f,count;
    fstream f2,f1;
    f2.open("B-large.txt",ios::in);
    f1.open("output.txt",ios::out);
  //cin>>t;
  cin>>t;
    i=1;
    while(i<=t)
    {
  cin>>s;
        count=0;
        c=s[0];
        for(j=1;s[j]!='\0';j++)
        {
            if(s[j]!=c )
            {
                if(s[j]=='-')
                count++;
                 c=s[j];

            }

        }
        if(s[0]=='-')
        {count++;
      cout<<"Case #"<<i<<": "<<2*count-1<<"\n";
      //f1<<"Case #"<<i<<": "<<2*count-1<<"\n";
        }
        else
        cout<<"Case #"<<i<<": "<<2*count<<"\n";
     //f1<<"Case #"<<i<<": "<<2*count<<"\n";
        i++;
    }
      return 0;
}
