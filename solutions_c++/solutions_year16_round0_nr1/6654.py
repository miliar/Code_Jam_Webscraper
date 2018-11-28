#include <iostream>
#include <fstream>
using namespace std;

int main()
{
freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
int t;
cin>>t;
long int n,f;
for(long int i=0;i<t;i++)
{

 // fprintf(stderr,"Case #%d:",i+1);
    int array_size=10;
    int a[array_size]={0,1,2,3,4,5,6,7,8,9};
    cin>>n;
 cout<<"Case #"<<i+1<<": ";
    if(n==0){
    cout<<"INSOMNIA"<<endl;
   //   fprintf(stderr,"INSOMNIA\n");
    }
    else{
        for(int j=1;;j++){
            long int e=n*j;
            while(e>0){
                f=e%10;
                e=e/10;

                for(int m=0;m<array_size;m++){
                    if(f==a[m]){

                        for(int q=m;q<array_size;q++){
                        a[q]=a[q+1];
                        }

                        array_size--;
                    }
                }

            }
            if(j==1000){
                cout<<"INSOMNIA"<<endl;
                //fprintf(stderr,"INSOMNIA\n");
                break;
            }
            if(array_size==0){
              // fprintf(stderr,"%d\n",n*j);
               cout<<n*j<<endl;
                break;
            }
        }
    }
}
    return 0;
}
