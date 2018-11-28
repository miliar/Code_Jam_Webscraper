#include <bits/stdc++.h>

using namespace std;

#define pb push_back

int main(){
	int t, npartidos;
	int caso=1;
	cin >> t;
	int p[60000];
	int val;
	while (t--)
	{
		vector<pair<int, int> > v;
		int sum=0;
		cin >> npartidos;
		for (int i = 0; i < npartidos; i++){
			cin >> val;
			v.pb({val, i});
			sum+=val;
		}
		string saida="";
		char a, b;
		int valA, valB;
		int meio;
		bool erro;
		int cnt;
		while(1){
			sort(v.begin(), v.end(), greater<pair<int, int> >());
			if(v.size()==0) break;
			/*
			for (int i = 0; i < v.size(); i++)
			{
				printf("%d %c    ", v[i].first, v[i].second+'A');
			}
			cout << endl;
			*/
			if(v.size()==1){
				saida+=' ';
				saida+=v[0].second+'A';
				break;
				
			}
			
			if(v.size()==2){
				if(v[0].first > v[1].first){
					val = v[0].first - v[1].first;
					while(val--){
						v[0].first--;
						saida+=' ';
						saida+=v[0].second+'A';
					
						if(v[0].first==0)
							v.erase(v.begin()+0);
						sum--;	
					}
					break;
				}
				else if(v[0].first < v[1].first){
					val = v[1].first - v[0].first;
					while(val--){
						v[1].first--;
						saida+=' ';
						saida+=v[1].second+'A';
					
						if(v[1].first==0)
							v.erase(v.begin()+0);
						sum--;	
					}
					break;
				}else{
					
					val = v[0].first;
					while (val--)
					{
						a=v[0].second+'A';
						b=v[1].second+'A'; 
						saida+=' ';
						saida+=a; saida+=b;					
					}
					break;
				}
			}else if(v.size()==3){
				if(v[0].first>1){
					meio = (sum-2)/2;
					erro=false;
					cnt=0;
					for (int i = 1; i < v.size(); i++)
					{
						if(v[i].first > meio) cnt++;
					}
					
					if(cnt==1) erro=true;
					if(!erro){
						saida+=' ';
						saida+=v[0].second+'A';
						saida+=v[0].second+'A';
						v[0].first-=2;
						if(v[0].first==0) v.erase(v.begin()+0);
						
						sum-=2;
					}else{
										
						saida+=' ';
						saida+=v[0].second+'A';
						v[0].first--;
						if(v[0].first==0) v.erase(v.begin()+0);
						
						sum--;	
					}
				}else{
									
					saida+=' ';
					saida+=v[0].second+'A';
					v[0].first--;
					if(v[0].first==0) v.erase(v.begin()+0);
					
					sum--;					
				}
				
			}else{//remove 1 de cada
				meio = (sum-2)/2;
				erro=false;
				cnt=0;
				for (int i = 2; i < v.size(); i++)
				{
					if(v[i].first > meio) cnt++;
				}
				
				if(cnt==1) erro=true;
				if(!erro){
					saida+=' ';
					saida+=v[0].second+'A';
					saida+=v[1].second+'A';
					v[0].first--;
					v[1].first--;
					if(v[0].first==0 && v[1].first==0){
						v.erase(v.begin()+0);
						v.erase(v.begin()+0);
					}else if(v[0].first==0) v.erase(v.begin()+0);
					else v.erase(v.begin()+1);
					
					sum-=2;
				}else{					
					saida+=' ';
					saida+=v[0].second+'A';
					v[0].first--;
					if(v[0].first==0) v.erase(v.begin()+0);
					
					sum--;	
				}
			}
				
			
		}
		
		printf("Case #%d:", caso++);	
		cout << saida << endl;
			
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
