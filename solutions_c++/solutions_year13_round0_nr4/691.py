#include "stdio.h"
#include <vector>
#include <algorithm>
using namespace std;

#define vi vector<int>
#define p1 pair<vi, bool>
#define p2 pair<int, p1>
#define vpvi vector<p2 >
#define vpvii vpvi::iterator
#define vpviri vpvi::reverse_iterator

int haveKs[201];
vector<pair<int, pair<vector<int>, bool> > > allB;
vi seq;

bool check() {
	int t=0;
	bool ret=false, cpt;
	vi ks;
	vpvii i;
	
	bool end=true;
//	for(int i=0; i<201;++i) {
		for(vpvii j=allB.begin(); j<allB.end(); ++j)
			if((*j).second.second==false) {
				end=false; break;
			}
//		if(!end) break;
//	}

	if(end) return true;

	bool fail=false;
	bool hvK;
	for(vpvii j=allB.begin(); j<allB.end();++j) {
		if((*j).second.second==false && haveKs[(*j).first]==0) {
			hvK=false;
			for(vpvii k=allB.begin(); k<allB.end();++k) {
				if((*k).first!=(*j).first && (*k).second.second==false) {
					for(vi::iterator l=(*k).second.first.begin(); l<(*k).second.first.end(); ++l) {
						if((*l)==(*j).first) {
							hvK=true; break;
						}
					}
				}
				if(hvK) break;
			}
			if(!hvK) return false;
		}
	}
	/*
	for(t=0; t<201; ++t) {
		if(haveKs[t]==0) {
			continue;
		}
		cpt=true;
		for(vpvii j=allB[t].begin(); j<allB[t].end(); ++j) {
			if((*j).second.second==false) {
				cpt=false; break;
			}
		}
		if(!cpt) break;
	}
	
	if(t==201) return false;
	*/

//	--haveKs[t];
//	bool selfI=false;
	for(i=allB.begin(); i<allB.end(); ++i) {
		//open
		if((*i).second.second) continue;
		t=(*i).first;
		if(haveKs[t]==0) continue;

		(*i).second.second=true;
		ks =(*i).second.first;
		--haveKs[t];

		for(vi::iterator j=ks.begin(); j<ks.end(); ++j) {
			++haveKs[*j];
//			if((*j) ==t) selfI=true;
		}
		
		//check
		if(check()) {ret=true;break;}

		//reset
		(*i).second.second=false;
		for(vi::iterator j=ks.begin(); j<ks.end(); ++j)
			--haveKs[*j];
		++haveKs[t];
//		if(selfI) break;
	}

//	if(!ret) ++haveKs[t];
	if(ret) seq.push_back(i-allB.begin()+1);

	return ret;
}

int main() {
	int T,N,K, T1,K1;
	int MAX;
	FILE *fp, *fp2;
	int tmp;
	vi tmvi;
	
	int Box[201], key[201];
	fp = fopen("D-small-attempt4.in", "r");
	fp2 = fopen("D-small-attempt4-sol.in", "w");
	fscanf(fp, "%d", &T);

	int selfK;
	for(int i=0; i<T; ++i) {
		for(int j=0;j<201;++j) Box[j]=key[j]=0;


		MAX=0;
		fprintf(fp2,"Case #%d: ",i+1);
		fscanf(fp,"%d %d", &K, &N);
		for(int j=0; j<201;++j) haveKs[j]=0;
		for(int j=0; j<K;++j) {
			fscanf(fp,"%d",&tmp);
			++haveKs[tmp];
			++key[tmp];
		}


		for(int j=0; j<N;++j) {
			selfK=0;
			fscanf(fp, "%d %d", &T1,&K1);
			if(T1>MAX) MAX=T1;
			++Box[T1];
			tmvi = vi();
			for(int k=0;k<K1;++k) {
				fscanf(fp, "%d", &tmp);
				if(tmp==T1) ++selfK;
				++key[tmp];
				tmvi.push_back(tmp);
			}
			allB.push_back(p2(T1, p1(tmvi, false)));
//			allB[T1].push_back(pvi(selfK, p2(p1(tmvi, j+1), false)));
		}

		++MAX;
//		for(int j=0; j<MAX; ++j) sort(allB[j].begin(), allB[j].end());

		bool enoughK=true;
		for(int j=0; j<MAX; ++j)
			if(key[j]<Box[j]) {enoughK=false; break;}
/*		int selfnum,knum;
		vpvi tmpv;
		vi::iterator tv2;
		for(int j=0; j<MAX; ++j) {
			if((selfnum=allB[j].size())==0) continue;
			knum=haveKs[j];
			for(int k=0;k<MAX;++k) {
				tmpv=allB[k];
				for(vpvii l=tmpv.begin(); l<tmpv.end(); ++l) {
					for(tv2=(*l).second.first.begin(); tv2<(*l).second.first.end(); ++tv2)
						if((*tv2)==j) ++knum;
				}
			}
			if(knum<selfnum){enoughK=false; break;}
		}
		*/
		if(!enoughK )	fprintf(fp2, "IMPOSSIBLE\n");
		else {
		//check
		if(check()) {
			for(vi::reverse_iterator j=seq.rbegin(); j<seq.rend(); ++j)
				if(j!=seq.rend()-1)
					fprintf(fp2, "%d ", *j);
				else fprintf(fp2, "%d\n", *j);
		}else {
			fprintf(fp2, "IMPOSSIBLE\n");
		}
		}

		//del
//		for(int j=0; j<201; ++j)
//			allB[j].clear();
		allB.clear();
		seq.clear();
	}

	fclose(fp);
	fclose(fp2);
	return 0;
}
