#include<fstream>
#include<algorithm>
#include <queue>
#include<vector>

using namespace std;

typedef struct{
	int num;
	int party;
}struc;

typedef struct
{
	int operator () (struc &a, struc &b){
		return a.num<b.num;
	}
}comp;

int main() {
	int n;
	ifstream is;
	is.open("A-large.in");
	ofstream os;
	os.open("outA.txt");
	is>> n;
	for(int j=0; j<n; j++) {
		int np;
        priority_queue<struc , vector<struc>, comp> pq;
		is>>np;
		int aux, cnt=0;
		for(int i=0;i<np; i++){
			is>>aux;
			cnt+=aux;
			struc a;
			a.num = aux;
			a.party = i;
			pq.push(a);
		}
		os<<"Case #"<<j+1<<": ";
		for(int i=0;i<cnt-2;){
			if((cnt-i)%2==1)
			{
				struc party = pq.top();
				pq.pop();
				party.num--;
				if(party.num>0)
					pq.push(party);
				os<<(char)((char)party.party + 'A')<<" ";
				i++;
			}
			else{
				struc party = pq.top();
				pq.pop();
				party.num--;
				if(party.num>0)
					pq.push(party);
				os<<(char)((char)party.party + 'A');
				i++;
				party = pq.top();
				pq.pop();
				party.num--;
				if(party.num>0)
					pq.push(party);
				os<<(char)((char)party.party + 'A')<<" ";
				i++;
			}
		}
		struc party = pq.top();
		pq.pop();
		party.num--;
		if(party.num>0)
			pq.push(party);
		os<<(char)((char)party.party + 'A');
		party = pq.top();
		pq.pop();
		party.num--;
		if(party.num>0)
			pq.push(party);
		os<<(char)((char)party.party + 'A')<<endl;
	}
	return 0;
}



