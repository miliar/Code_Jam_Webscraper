#include <bits/stdc++.h>
using namespace std;
int n;
string panqueques;
int a;
int cambios[500];


int main(){
	cin>>n;
	
	for (int i = 0; i < n; ++i)
	{
		cin>>panqueques;
	    a = panqueques.size();
	    
			

		for (int nu = 1; nu < a; nu++){
			

			if ( panqueques [nu] != panqueques[nu-1])
		{
			cambios[i]++;
		}

		
		 

		}
		
		if (panqueques[a-1] =='-')
		{
			cambios[i]++;
		}

		cout<<"Case #"<<(i+1)<<": "<<cambios[i]<<endl;
		 
	}


}