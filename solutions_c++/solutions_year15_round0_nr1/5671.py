#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
* compare
*/
struct input{
    int Smax;
    string auden;
    };
void  proccess(struct input *in, int T) {
     for(int i=0;i<T;i++)
     {
         int need=0;
         int audlen = in[i].Smax + 1;
         string aud = in[i].auden;
         for(int j=0;j<audlen;j++)
         {
             if(0==j)
             {
                 if(aud[j]=='0')need+=1;
             }
             else
             {
                 if(aud[j]!='0')
                 {
                     int tmps=0;

                     for(int k=0;k<j;k++)
                          tmps+=(aud[k]-'0');
                     if((tmps+need)<j)need+=(j-(tmps+need));
                 }
             }
         }

         cout<<"Case #"<<(i+1)<<": "<<need<<endl;
     }

    
    }


int main()
{
    int T;
    cin>>T;
    struct input inp[T];
    for(int i=0;i<T;i++)
    {
        cin>>inp[i].Smax>>inp[i].auden;

    }
    proccess(inp,T);


return 0;
}
