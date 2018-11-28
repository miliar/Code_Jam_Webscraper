#include <iostream>
#include <fstream>
using namespace std;

int N;
long long int temp;
bool list[10],keep=true;
int main()
{
	int T;cin>>T;
	for(int t=0;t<T;t++){
	  int i=0;
	  keep=true;
	  for(i=0;i<10;i++)
	    list[i]=false;
	  cin>>N;
	  cout<<"Case #"<<t+1<<": ";
	  if(N==0){
	    cout<<"INSOMNIA\n";
	    continue;
	  }
	  
	  i=0;
	  while(keep){
		  temp=i*N;
		  keep=false;
		  while(temp>0)
		  {
		    list[temp%10]=true;
		    temp/=10;
		  }
		  for(int j=0;j<10;j++){
		    if(list[j]==false)
		    {
		      keep=true;
		    }
		  }
		  i++;
	  }
	  cout<<(i-1)*N<<endl;
	    
	}
	return 0;
}
