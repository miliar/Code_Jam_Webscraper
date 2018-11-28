#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#define VECINT std::vector<int>
#define ULL unsigned long long int
#define PII std::pair<ULL,ULL>
#define VECPII std::vector<PII>
#define CI const_iterator

bool jestPalindromem(ULL a);

class FS{
	public:
		FS(int h);
		int wPrzedziale(int a, int b)const;
	private:
		VECINT itsTab;
};

class SQRT{
	public:
		SQRT(ULL M);
		int operator() (ULL a,bool wDol = false) const;
	private:
		VECPII S;
};

SQRT::SQRT(ULL M){
	S.reserve(10000000);
	ULL i;
	for(i = 1; i*i<=M;++i)
		S.push_back(PII(i*i,i));
		
	S.push_back(PII(i*i,i));
}

int SQRT::operator () (ULL a, bool wDol ) const{
	VECPII::CI iF = std::lower_bound(this->S.begin(),this->S.end(),PII(a,0));
	
	if(iF->first==a || !wDol)
		return iF->second;
	else
		return (--iF)->second;
}

FS::FS(int h):
itsTab(h+1,0)
{
	for(ULL i = 1 ; i <= (unsigned int)h; ++i){
		itsTab[i] = itsTab[i-1];
		if(jestPalindromem(i)&&jestPalindromem(i*i))
			itsTab[i] += 1;

	}
}

int FS::wPrzedziale(int a, int b) const{
	return this->itsTab[b]-this->itsTab[a-1];
}
	

int main(){
	std::ios_base::sync_with_stdio(false);
	
	int T;
	std::cin >> T;
	VECPII D(T);
	ULL max=0;
	
	for(int i = 0 ; i < T; ++i){
		std::cin >> D[i].first >> D[i].second;
		max = std::max(max,D[i].second);
	}
	
	SQRT mSQRT(max);
	FS mFS(mSQRT(max));
	
	
	for(int i = 0; i < T; ++i)
		std::cout << "Case #" << (i+1) << ": "<<  mFS.wPrzedziale(mSQRT(D[i].first),mSQRT(D[i].second,true)) << std::endl;
		
	
	
	return 0;
}

bool jestPalindromem(ULL a){
	std::stringstream ss;
	ss << a;
	
	std::string s = ss.str();
	
	for(unsigned int i = 0; i < s.length()/2; ++i)
		if(s[i]!=s[s.length()-1-i])
			return false;
			
	return true;
}
