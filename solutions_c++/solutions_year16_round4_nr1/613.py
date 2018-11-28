#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;
class nodes{
public:
	int lson,rson;
	char winner;
	int depth;
};
int num=0;
void Gao()
{
	printf("Case #%d: ",++num);
	vector<nodes> treer,treep,trees;
	int N;
	int R,P,S;
	string temr="",temp="",tems="";
	cin>>N>>R>>P>>S;
	//winner R
	nodes rootr;
	rootr.depth=0;rootr.lson=-1;rootr.rson=-1;rootr.winner='R';
	treer.push_back(rootr);
	int st=0;
	while(true){
		if(treer[st].winner=='R'){
			nodes t1,t2;
			t1.depth=treer[st].depth+1;t1.winner='R';
			t2.depth=treer[st].depth+1;t2.winner='S';
			treer.push_back(t1);treer.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(treer[st].winner=='P'){
			nodes t1,t2;
			t1.depth=treer[st].depth+1;t1.winner='P';
			t2.depth=treer[st].depth+1;t2.winner='R';
			treer.push_back(t1);treer.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(treer[st].winner=='S'){
			nodes t1,t2;
			t1.depth=treer[st].depth+1;t1.winner='P';
			t2.depth=treer[st].depth+1;t2.winner='S';
			treer.push_back(t1);treer.push_back(t2);
			if(t1.depth>N)
				break;
		}
		st++;
	}
	int rp=0,rr=0,rs=0;
	for (int i=0;i<treer.size();i++){
		if (treer[i].depth==N)
			temr=temr+treer[i].winner;
	}
	for (int i=0;i<temr.length();i++){
		if (temr[i]=='R')
			rr++;
		if (temr[i]=='P')
			rp++;
		if (temr[i]=='S')
			rs++;
	}
	for (int i=0;i<N;i++)
	{
		int base=0;
		int halflen=pow(2,i);
		while(base<temr.length()){
			string tt1=temr.substr(base,halflen);
			string tt2=temr.substr(base+halflen,halflen);
			if(tt1>tt2){
				for (int j=0;j<halflen;j++)
					temr[j+base]=tt2[j],temr[j+base+halflen]=tt1[j];
			}
			base+=2*halflen;
		}
	}
	
	//winner P
	nodes rootp;
	rootp.depth=0;rootp.lson=-1;rootp.rson=-1;rootp.winner='P';
	treep.push_back(rootp);
	st=0;
	while(true){
		if(treep[st].winner=='R'){
			nodes t1,t2;
			t1.depth=treep[st].depth+1;t1.winner='R';
			t2.depth=treep[st].depth+1;t2.winner='S';
			treep.push_back(t1);treep.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(treep[st].winner=='P'){
			nodes t1,t2;
			t1.depth=treep[st].depth+1;t1.winner='P';
			t2.depth=treep[st].depth+1;t2.winner='R';
			treep.push_back(t1);treep.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(treep[st].winner=='S'){
			nodes t1,t2;
			t1.depth=treep[st].depth+1;t1.winner='P';
			t2.depth=treep[st].depth+1;t2.winner='S';
			treep.push_back(t1);treep.push_back(t2);
			if(t1.depth>N)
				break;
		}
		st++;
	}
	int pp=0,pr=0,ps=0;
	for (int i=0;i<treep.size();i++){
		if (treep[i].depth==N)
			temp=temp+treep[i].winner;
	}
	for (int i=0;i<temp.length();i++){
		if (temp[i]=='R')
			pr++;
		if (temp[i]=='P')
			pp++;
		if (temp[i]=='S')
			ps++;
	}
	
	for (int i=0;i<N;i++)
	{
		int base=0;
		int halflen=pow(2,i);
		while(base<temp.length()){
			string tt1=temp.substr(base,halflen);
			string tt2=temp.substr(base+halflen,halflen);
			if(tt1>tt2){
				for (int j=0;j<halflen;j++)
					temp[j+base]=tt2[j],temp[j+base+halflen]=tt1[j];
			}
			base+=2*halflen;
		}
	}
	
	//winner S
	nodes roots;
	roots.depth=0;roots.lson=-1;roots.rson=-1;roots.winner='S';
	trees.push_back(roots);
	st=0;
	while(true){
		if(trees[st].winner=='R'){
			nodes t1,t2;
			t1.depth=trees[st].depth+1;t1.winner='R';
			t2.depth=trees[st].depth+1;t2.winner='S';
			trees.push_back(t1);trees.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(trees[st].winner=='P'){
			nodes t1,t2;
			t1.depth=trees[st].depth+1;t1.winner='P';
			t2.depth=trees[st].depth+1;t2.winner='R';
			trees.push_back(t1);trees.push_back(t2);
			if(t1.depth>N)
				break;
		}
		if(trees[st].winner=='S'){
			nodes t1,t2;
			t1.depth=trees[st].depth+1;t1.winner='P';
			t2.depth=trees[st].depth+1;t2.winner='S';
			trees.push_back(t1);trees.push_back(t2);
			if(t1.depth>N)
				break;
		}
		st++;
	}
	int sp=0,sr=0,ss=0;
	for (int i=0;i<trees.size();i++){
		if (trees[i].depth==N)
			tems=tems+trees[i].winner;
	}
	for (int i=0;i<tems.length();i++){
		if (tems[i]=='R')
			sr++;
		if (tems[i]=='P')
			sp++;
		if (tems[i]=='S')
			ss++;
	}
	
	for (int i=0;i<N;i++)
	{
		int base=0;
		int halflen=pow(2,i);
		while(base<tems.length()){
			string tt1=tems.substr(base,halflen);
			string tt2=tems.substr(base+halflen,halflen);
			if(tt1>tt2){
				for (int j=0;j<halflen;j++)
					tems[j+base]=tt2[j],tems[j+base+halflen]=tt1[j];
			}
			base+=2*halflen;
		}
	}
	
	int ok=-1;
	string best="";
	if (rr==R&&rp==P&&rs==S){
		if (ok==-1)
			best=temr,ok=1;
		else{
			if (temr<best)
				best=temr;
		}
	}
	if (pr==R&&pp==P&&ps==S){
		if (ok==-1)
			best=temp,ok=1;
		else{
			if (temp<best)
				best=temp;
		}
	}
	if (sr==R&&sp==P&&ss==S){
		if (ok==-1)
			best=tems,ok=1;
		else{
			if (tems<best)
				best=tems;
		}
	}
	if(ok==-1)
		cout<<"IMPOSSIBLE"<<endl;
	else
		cout<<best<<endl;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	num=0;
	cin>>T;
	while(T--)
		Gao();
	return 0;
} 
