#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
* compare
*/
struct input{
    int x,r,c;
    };
void  proccess(struct input *in, int T) {
     for(int i=0;i<T;i++)
     {
        string res;
        int x= in[i].x,r=in[i].r,c=in[i].c;
        if(r*c<x)
        {
            res ="RICHARD";
        }
        else if(r*c==x)
        
        {   
            if(x==1||x==2)
            res="GABRIEL";
            else if(x==3)
            {
                
                    res="RICHARD";
            }else if(x==4)
            {
                
                    res="RICHARD";
                
            }
        }
        else
        {
        if((r*c)%(x)!=0)
        {res = "RICHARD";}
        else 
        {   if(x==1)
               res="GABRIEL";
            else if(x==2)
            {
                res="GABRIEL";

            }else if(x==3)
            {
                res="GABRIEL";
            }else if(x==4) 
            {
            if((r==2||c==2))res="RICHARD";
            else res="GABRIEL";
            }
        }
        }   
         cout<<"Case #"<<(i+1)<<": "<<res<<endl;
     }

    
    }


int main()
{
    int T;
    cin>>T;
    struct input inp[T];
    for(int i=0;i<T;i++)
    {
        cin>>inp[i].x>>inp[i].r>>inp[i].c;

    }
    proccess(inp,T);


return 0;
}
