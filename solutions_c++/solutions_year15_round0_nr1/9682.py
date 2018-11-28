#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
      int T,sm,n;
      string a;
      int totalno=0,ppladded=0;
      cin>>T;
      for(int i=0;i<T;i++){
	    totalno=0;
	    ppladded=0;
	    cin>>sm;
	    cin>>a;
	    for(int j=0;j<=sm;j++){
		  n=int(a[j])-48;
		  // cout<<n<<endl;
		  if(totalno>=j){
			totalno+=n;
			//	cout<<n<<"\t"<<totalno<<endl;
		  }
		  else if(n){
			ppladded=ppladded+j-totalno;
			totalno+=(ppladded+n);
		  }
	    }
	    printf("Case #%d: %d\n",i+1,ppladded);
      }
}
