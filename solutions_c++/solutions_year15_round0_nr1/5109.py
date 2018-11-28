#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("input.txt", "r" , stdin );
    freopen("output.txt", "w" , stdout );
    	int t;
	scanf("%d",&t);
	int j =0;
	while(t--){

		int smax ;
		string st;
		scanf("%d",&smax);
		cin>>st;
		//cout<<st;
		char ch[1005];
		strcpy(ch , st.c_str());
		int i , count=0 ;
		int l = strlen(ch);
		int a[1005];
		for(int  k =0 ; k< l ;k++)
		{
			a[k] = ch[k]-'0';
		}
			
		j++;
		if(l == 1 && ch[0] == '1')
			cout<<"Case #"<<j<<": 0\n";
		else
		{
		for ( i = 1; i < l; i++)
		{

               int y = a[i-1];
             
				if(y>=i){

					a[i]= a[i] + a[i-1];

					}
					else
					{
					   
						count++;
						a[i] = a[i] + a[i-1]+ 1;
						
					}
		}
		cout<<"Case #"<<j<<": "<<count<<"\n";
	}

	}
	return 0;
}

