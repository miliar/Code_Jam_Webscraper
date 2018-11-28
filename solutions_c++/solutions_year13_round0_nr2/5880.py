#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int t,m,k,b,c,**save,*maxm,*maxk,counter;
	bool flag;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>m>>k;
		maxm=new int[m];
		maxk=new int[k];
		fill(maxm,maxm+m,0);
		fill(maxk,maxk+k,0);
		save=new int *[m];
		for(b=0;b<m;++b){
			save[b]=new int[k];
			for(c=0;c<k;++c){
				cin>>save[b][c];
				if(save[b][c]>maxm[b])
					maxm[b]=save[b][c];
				if(save[b][c]>maxk[c])
					maxk[c]=save[b][c];
			}
		}
		for(b=0,flag=true;b<m&&flag;++b){
			for(c=0;c<k;++c){
				if(save[b][c]!=maxm[b]&&save[b][c]!=maxk[c]){
					flag=false;
					break;
				}
			}
		}
		if(flag)
			cout<<"Case #"<<counter<<": YES"<<endl;
		else
			cout<<"Case #"<<counter<<": NO"<<endl;
		for(b=0;b<m;++b)
			delete [] save[b];
		delete [] save;
	}
	return 0;
}
