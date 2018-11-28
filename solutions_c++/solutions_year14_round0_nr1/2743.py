 #include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);

  using namespace std;

  int a[5][5],b[5][5];
  bool is[18];
  int main() { _
  	// freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
  	int t,i,j,k,l,n,m,it;
  	cin>>t;
  	for(it=1;it<=t;it++){
      for(i=0;i<18;i++)
        is[i]=false;
  		cin>>n;
  		for(i=0;i<4;i++){
  			for(j=0;j<4;j++){
  				cin>>a[i][j];
  			}
  		}
  		cin>>m;
  		for(i=0;i<4;i++){
  			for(j=0;j<4;j++){
  				cin>>b[i][j];
  			}
  		}
  		l=0;
  		for(i=0;i<4;i++){
  			is[a[n-1][i]]=true;
  		}
  		for(i=0;i<4;i++){
  			if(is[b[m-1][i]]){
  				l++;
  				k=b[m-1][i];
  			}
  		}
  		if(l==1){
  			cout<<"Case #"<<it<<": "<<k<<endl;
  		}
  		else if(l>1){
  			cout<<"Case #"<<it<<": Bad magician!"<<endl;
  		}
      else{
        cout<<"Case #"<<it<<": Volunteer cheated!"<<endl;
      }
  	}
    return 0;
  }