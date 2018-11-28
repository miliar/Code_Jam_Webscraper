#include <iostream>

using namespace std;
int dexists(int *a,int k)
{
    if(a[0]==-1)
        return 1;
    for(int i=0;a[i]!=-1;i++)
    {
        if(a[i]==k)
            return 0;
    }
    return 1;
}
void insomnia(int N,int in)
{
    int arr[10];
    for(int i=0;i<10;i++)
        arr[i]=-1;
    int j=0;
    int x=N;
    while(1)
    {
        if(N<=0)
        {
           cout<<"Case #"<<in<<": INSOMNIA"<<endl;
    break;
        }
        if(j==10)
        {
            cout<<"Case #"<<in<<": "<<N-x<<endl;
            break;
        }
        else
        {

            int t=N;
          while(t!=0)
            {
                if(dexists(arr,t%10))
                {
                arr[j]=t%10;
                j++;
                }
                t=t/10;
            }
      }
     N=N+x;
    }
}
int main()
{
    int T;
    cin>>T;
    int arrin[T];
    for(int i=0;i<T;i++)
    cin>>arrin[i];
    for(int i=0;i<T;i++)
    insomnia(arrin[i],i+1);
    return 0;
}
