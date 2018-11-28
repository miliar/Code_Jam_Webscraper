/*
 * b.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: aki
 */
#include<cstdlib>
#include<cstdio>
#include<vector>
using namespace std;

vector<char> sazimanjeVektora(vector<char>  v){
	vector<char> v1;
	int size = v.size();
	int k=0,p=1;
	v1.push_back(v[k]);

	while(p<v.size()){
		while(v[k]==v[p]&&p<v.size())p++;
		if(p>=v.size())break;
		v1.push_back(v[p]);
		k=p;
		p=k+1;
	}

	return v1;

}
int main(){
	freopen("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);

	int T, t;
	scanf("%d\n", &T);
	T++;


	for(t=1;t<T;t++){
		vector<char> v;
		char c;
		scanf("%c",&c);
	bool nijeKraj=false;
	while(c!='\n'&&!nijeKraj){
		v.push_back(c);
		nijeKraj=scanf("%c",&c)==EOF;

	}
	v=sazimanjeVektora(v);
	int rez=0;

	while(v.size()>1){
		if(v[0]=='-'){
			rez+=1;
			v[0]='+';
		}else{
			rez+=2;
			v[1]='+';
		}
		v=sazimanjeVektora(v);

	}
	if(v[0]=='-')rez++;




		printf("Case #%d: %d \n",t, rez);
	}

}



