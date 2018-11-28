#include <iostream> 
using namespace std;
int magia(int); 
int main() 
{
  int t,n;
  cin>>t; 
  for(int i=1;i<=t;++i) 
  {
    cin>>n;
    if(n>=0&&n<=200)
    {
    	if(n==0)
	    cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    	else 
            cout << "Case #" << i << ": " <<magia(n)<< endl;
    }
    else{i--;t--;}
  }
}
int magia(int n)
{
   int ok[10]={0},tmp,cnt=0;
   for(int i=1;;i++)
   {
        tmp=n*i;
   	do{
		ok[tmp%10]++;
		tmp/=10;
   	}while(tmp);
       for(int k=0;k<10;k++)
	  if(ok[k]>0)
		cnt++;
          else
		continue;
       if(cnt==10)
	 return n*i;
       else cnt=0;
   }
}
