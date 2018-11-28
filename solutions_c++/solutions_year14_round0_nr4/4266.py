#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	//READ("D-large.in");
   // WRITE("D-large.out");
	int x,old=0,New=0,num;
	vector<double>nam;
	vector<double>ken;
	cin>>num;
	for(int k=0;k<num;k++){
	cin>>x;
	int m=x;
	nam.resize(x);
	ken.resize(x);
	for(int i=0;i<x;i++)
    	cin>>nam[i];
	for(int i=0;i<x;i++)
    	cin>>ken[i];
	sort(ken.begin(),ken.end());
	sort(nam.begin(),nam.end());
	int j=0,i=0;
	while(j<m){
		if(nam[j]>ken[i]){
			i++;j++;
			New++;
	    }
	    else if(nam[j]<ken[i]){
	    	j++;
	    }
	    else if(nam[j]==ken[i]){
	    	j++;i++;
     	}
    }
     j=0,i=0;
	while(i<m){
		if(nam[j]>ken[i]){
			i++;
			old++;
	    }
	    else if(nam[j]<ken[i]){
	    	j++;i++;
	    }
	    else if(nam[j]==ken[i]){
	    	j++;i++;
     	}
    }
    cout<<"Case #"<<k+1<<": "<<New<<" "<<old<<endl;
    nam.clear();
    ken.clear();
    old=0;
    New=0;
    }
}
