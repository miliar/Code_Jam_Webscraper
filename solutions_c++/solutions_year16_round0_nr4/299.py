// topcoder.cpp : �R���\�[�� �A�v���P�[�V�����̃G���g�� �|�C���g���`���܂��B
//

#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <unordered_map>
#include "assert.h"

using namespace std;

static const double EPS = 1e-9;
template<class T> bool INRANGE(T x,T a,T b){return a<=x&&x<=b;}
template<class T> void amin(T &a,T v){if(a>v) a=v;}
template<class T> void amax(T &a,T v){if(a<v) a=v;}
int ROUND(double x) { return (int)(x+0.5); }
bool ISINT(double x) { return fabs(ROUND(x)-x)<=EPS; }
bool ISEQUAL(double x,double y) { return fabs(x-y)<=EPS*max(1.0,max(fabs(x),fabs(y))); }
double SQSUM(double x,double y) { return x*x+y*y; }
#define PI  (acos(-1))
#define ARRAY_NUM(a) (sizeof(a)/sizeof(a[0])) 
#define NG (-1)
#define BIG ((int)1e9)
#define BIGLL ((ll)4e18)
#define SZ(a) ((int)(a).size())
#define SQ(a) ((a)*(a))
typedef unsigned long long ull;
typedef long long ll;

#define PRINTF(fmt,...) fprintf(stderr,fmt,__VA_ARGS__); printf(fmt,__VA_ARGS__);


#if 1


int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		ll K, C, S;
		cin >> K >> C >> S;

		ll powK[1000]={};
		powK[0]=1LL;
		for (int i = 1; i < 1000; ++i)
		{
			powK[i] = powK[i-1] * K;
		}

		const int s = (K+(C-1))/C; // �K�v��
		if(S>=s)
		{
			PRINTF("Case #%d:",testcase+1);

			for (int i = 0; i < s; ++i)
			{
				ll ans = 1;
				for(int p = 0; p < C && p + i * C < K; ++p)
				{
					ans += powK[C-1-p] * (p + i * C);
				}
				PRINTF(" %lld",ans);
			}

			PRINTF("\n");
		}
		else
		{
			PRINTF("Case #%d: IMPOSSIBLE\n",testcase+1);
		}
	}

	return 0;
}


#elif 1

// �e�X�gD
#if 0
string func(const string& s, const string& original)
{
	const int K = SZ(original);
	string ret;
	for (int i = 0; i < SZ(s); ++i)
	{
		if(s[i]=='L')
		{
			ret += original;
		}
		else
		{
			ret += string(K, s[i]);
		}
	}

	return ret;
}
#endif


int main(){

#if 0
	int N = 5;
	for(int i=0;i<1<<N;++i)
	{
		string original;

		int numG = 0;
		for(int b=0;b<N;b++)
		{
			if(i & (1<<b))
			{
				numG++;
			}
		}

		if(numG!=1) continue;


		for(int b=0;b<N;b++)
		{
			if(i & (1<<b))
			{
				original += string(1,char('0'+b));
			}
			else
			{
				original += "L";
			}
		}

		string s(original);
		int K = SZ(s);
		for (int depth = 0; depth < 2; ++depth)
		{
//			cerr << s << endl;
			s = func(s,original);
		}
		cerr << s << endl;
	}

	return 0;
#endif
	

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		int K, C, S;
		cin >> K >> C >> S;


		int a = 0;



		PRINTF("Case #%d: %d\n",testcase+1, a);
	}

	return 0;
}





#elif 1

int modpow(ll p, ll q, int MOD)
{
	ll res = 1;
	ll basemod = p%MOD;

	for(ll i=0;i<63;i++)
	{
		if( q & (1LL<<i))
		{
			res *= basemod;
			res = res%MOD;
		}
		basemod = (basemod*basemod)%MOD;
	}

	return (int)(res%MOD);
}

int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		PRINTF("Case #%d:\n",testcase+1);

		int N, J;
		cin >> N >> J;

		set < pair <ll, vector <ll> > > st;

		for (ll i = 0; i < 1LL<<(N-1); ++i)
		{
			if(i%2==0) continue;

			bool allDivided = true;

			vector <ll> divs;
			for(ll base=2; base<=10; ++base)
			{
				ll x = 0;
				ll acbase = 1;
				for (ll b = 0; b < N; ++b)
				{
					if (i & (1LL<<b))
					{
						x += acbase;
					}
					acbase *= base;
				}
				
				bool ok = false;
				for(ll div=2; div<=11; ++div)
				{
					if( (x+modpow(base, N-1, div))%div==0)
					{
						divs.push_back(div);
						ok = true;
						break;
					}
				}

				if(!ok)
				{
					allDivided = false;
				}
			}

			if(allDivided)
			{
				st.insert(make_pair(i, divs));
			}

			if(SZ(st)==J)
			{
				break;
			}
		}

		

		for (const auto& a : st)
		{
//			cout << a.first;


			string bits;
			ll tmp = a.first;
			while(tmp)
			{
				if(tmp%2)
				{
					bits = "1" + bits;
				}
				else
				{
					bits = "0" + bits;
				}

				tmp /= 2;
			}

			string s = "1" + string(N-1-SZ(bits), '0') + bits;

			cout << s;

			for (int i = 0; i < SZ(a.second); ++i)
			{
				cout << " ";
				cout << a.second[i];
			}

			cout << endl;
		}
	}

	return 0;
}


#elif 1

int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		string s;
		cin >> s;

		int a = 0;

		for (int i = 0; i < SZ(s)-1; ++i)
		{
			if(s[i]!=s[i+1])
			{
				a++;
			}
		}

		if(s[0]=='-' ^ (a%2))
		{
			a++;
		}

		PRINTF("Case #%d: %d\n",testcase+1, a);
	}

	return 0;
}



#elif 1

int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

#if 1
	for (int testcase = 0; testcase < T; ++testcase)
	{
		ll n;
		scanf("%lld ",&n);
#else

	int testcase = 0;
	for (ll n=1;n<=1e6;++n)
	{

#endif
		if(n==0)
		{
			PRINTF("Case #%d: INSOMNIA\n",testcase+1);
		}
		else
		{
			bool checked[10]={};
			for(ll x=1;;++x)
			{
				ll tmp = n*x;
				string s = to_string(tmp);
				for (char c : s)
				{
					checked[c-'0']=true;
				}

				if(count(&checked[0], &checked[10], false)==0)
				{
					PRINTF("Case #%d: %s\n",testcase+1, s.c_str());
					break;
				}
			}
		}
	}

	return 0;
}


#elif 0

// --------- T�̎����� -----------
// template < class STATE, class PARENT >
// class SAAttackerMove
// {
// public:
// 	void	saInit(STATE& currentState, const PARENT* parent) {};
// 	double	saScore(STATE& currentState, const PARENT* parent) { return 0.0; };
// 	void	saMove(STATE& currentState, const PARENT* parent) {};
// 	void	saResume(STATE& currentState, const PARENT* parent) {};
// };
//
// --------- SimulatedAnnealing�̎g�p�� --------- 
//	SimulatedAnnealing < SAAttackerMove <vector <EDir>, CodeVSAI>, vector <EDir>, CodeVSAI > *sa = new SimulatedAnnealing < SAAttackerMove <vector <EDir>, CodeVSAI>, vector <EDir>, CodeVSAI >(this);
//	sa->run();
//	delete sa;

// SimulatedAnnealing < SAUntangle, StateUntangle, SmallPolygons > *sa = new SimulatedAnnealing < SAUntangle, StateUntangle, SmallPolygons >(this);
// {
// 	sa->runNumLoops(min(10000000, pow(SZ(ss.mSubPnts), 2))); // �Ƃɂ����Œ���ł悢�B
// 	StateUntangle st = sa->getBestState();
// 
// 	const double score = sa->getBestScore();

//

class RandXor
{
public:
	RandXor()
	{
		init();
	}

	void init()
	{
		x=123456789;
		y=362436069;
		z=521288629;
		w= 88675123;
	}

	inline unsigned int random()
	{
		unsigned int t;
		t=(x^(x<<11));x=y;y=z;z=w; return( w=(w^(w>>19))^(t^(t>>8)) );
	}
private:
	unsigned int x;
	unsigned int y;
	unsigned int z;
	unsigned int w;
};

#ifdef _MSC_VER
#include <Windows.h>
ll getTime() {
	return GetTickCount();
}

// static double timeSlower = 0.205;

#else
#include <sys/time.h>
unsigned long long getTime() {
	struct timeval tv;
	gettimeofday(&tv, NULL);
	unsigned long long  result =  tv.tv_sec * 1000LL + tv.tv_usec / 1000LL;
	return result;
}

// static double timeSlower = 1.0;

#endif

static RandXor  randxor;    // �}���`�X���b�h�Ή��ɂ���Ȃ�A�؂��Ƃɗ����p�I�u�W�F�N�g��p�ӂ��āA�V�[�h��ς��܂��傤�B




vector <vector <int> > adj;
ll c[1005][35];

int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);
	for (int testcase = 0; testcase < T; ++testcase)
	{
		int N,K;
		ll P;
		scanf("%d %d %lld",&N,&K,&P);

		memset(c,0,sizeof(c));
		for (int i = 0; i < N; ++i)
		{
			for (int k = 0; k < K; ++k)
			{
				scanf("%lld",&c[i][k]);
			}
		}

		adj.clear();
		adj.resize(N);
		for (int i = 0; i < N-1; ++i)
		{
			int x,y;
			scanf("%d %d",&x,&y);

			adj[x-1].push_back(y-1);
			adj[y-1].push_back(x-1);
		}

		vector <int> currentState(N,0);
		ll currentScore = 0;
		ll bestScore = BIGLL;
		for (int i = 0; i < N; ++i)
		{
			currentScore += c[i][currentState[i]];

			int freq[40]={};
			for (int k = 0; k < SZ(adj[i]); ++k)
			{
				freq[currentState[adj[i][k]]]++;
				if(freq[currentState[adj[i][k]]]>=2)
				{
					currentScore += P;
					break;
				}
			}
		}
	

		const ll		msec = 1000;
		{
			const ll saTimeStart = getTime();            // �Ă��Ȃ܂��J�n�����BgetTime�́A���Ԃ�Ԃ��֐�
			const ll saTimeEnd = saTimeStart + msec;     // �Ă��Ȃ܂��I�������Bm_startTime�͂��̃v���O�������̂̊J�n����
			ll saTimeCurrent = saTimeStart;          // ���݂̎���

			int numLoops;
			while ((saTimeCurrent = getTime()) < saTimeEnd) // �Ă��Ȃ܂��I�������܂Ń��[�v
			{
				for (int saloop = 0; saloop < 100; ++saloop)
				{

					int x = randxor.random()%N;
					int m = randxor.random()%K;

					int backc = currentState[x];
					currentState[x] = m;

					ll nextScore = 0;
					for (int i = 0; i < N; ++i)	
					{
						nextScore += c[i][currentState[i]];

						int freq[40]={};
						for (int k = 0; k < SZ(adj[i]); ++k)
						{
							freq[currentState[adj[i][k]]]++;
							if(freq[currentState[adj[i][k]]]>=2)
							{
								nextScore += P;
								break;
							}
						}
					}

					// �ŏ�t=0�̂Ƃ��́A�X�R�A���ǂ��Ȃ낤�������Ȃ낤���A���next���g�p
					// �Ō�t=T�̂Ƃ��́A�X�R�A�����P�����Ƃ��̂݁Anext���g�p
					//					const ll duration = saTimeEnd - saTimeStart;         // �Ă��Ȃ܂��ɂ����鎞��
					//					const ll t = saTimeCurrent - saTimeStart;     // �Ă��Ȃ܂��@�J�n����̎���
					//					const ll R = 10000;
					// �X�R�A�������Ȃ����Ƃ��ł��A���̏�ԂɈړ�����J�ڂ���ꍇ��true�B�P���֐����g�p�B
					// TODO! exp�o�[�W�������������I
					const bool FORCE_NEXT = false; // R*(duration - t) > duration*(mXor.random() % R);

					// �X�R�A���ǂ��Ȃ��� or �����Ȃ��Ă������J��
					if (nextScore < currentScore || FORCE_NEXT)
					{
						currentScore = nextScore;
						//				fprintf(stderr,"current Score=%.8f time=%lld\n", currentScore, t);
					}
					else
					{
						currentState[x] = backc;
					}

					// �x�X�g�X�R�A�͕ۑ����Ă����B
					if (currentScore < bestScore)
					{
						bestScore = currentScore;
					}
				}
			}
		}


		PRINTF("Case #%d: %lld\n",testcase+1, bestScore);


	}
}

#elif 0


// �񍀊m���iBinomial Probability�j
const int COMB_MAX_N = 3005;
const int COMB_MAX_K = 3005;
static long double binoProb[COMB_MAX_N][COMB_MAX_K];	// n��̎��s�Ő����m��p��k�񐬌�
static long double binoMoreK[COMB_MAX_N][COMB_MAX_K];	// n��̎��s�Ő����m��p��k��ȏ㐬��

void init_binomialProb(long double p)
{
	binoProb[0][0]=1;
	binoProb[1][0]=1-p;
	binoProb[1][1]=p;
	for(int i=2;i<COMB_MAX_N;i++)
	{
		binoProb[i][0]=binoProb[i-1][0]*(1-p);
		for(int k=1;k<COMB_MAX_K;k++)
		{
			binoProb[i][k]=(binoProb[i-1][k]*(1-p)+binoProb[i-1][k-1]*p);
		}
	}

	for(int i=0;i<COMB_MAX_N;i++)
	{
		binoMoreK[i][COMB_MAX_K-1]=0.0;
		for(int k=COMB_MAX_K-2;k>=0;k--)
		{
			binoMoreK[i][k] = binoMoreK[i][k+1] + binoProb[i][k];
		}
	}
}

int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		long double ans = 0;
		int N,K;
		long double p;
		scanf("%d %d %lf",&N,&K,&p);
		init_binomialProb(p);



		// dp[���܂܂łӂ�������]=���Ғl
		vector < long double > dp(3100);
		for (int i = 0; i <= N; ++i)
		{
			// i���ӂ�����A
			for (int k = 1; k <= N-i; ++k)
			{
				amax(dp[i+k], dp[i]+binoMoreK[k][K]);
			}
		}

		PRINTF("Case #%d: %.25f\n",testcase+1, dp[N]);
	}

	return 0;
}


#else
int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int testcase = 0; testcase < T; ++testcase)
	{
		int N;
		string A,B;
		cin >> N >> A >> B;

		vector < vector < int > > dp(N+1, vector <int>(2, BIG));

		vector < int > rev(N+1);
		rev[N]=0;
		rev[N-1]=1;
		for (int i = N-2; i >= 0; --i)
		{
			rev[i] = rev[i+1] + (B[i]==B[i+1]?0:1);
		}

		// 
		// dp[�����ʒu][���ɍ��h��Ԃ��͈̔͂��I����=1]=�h������
		dp[0][0]=0;
		dp[0][1]=0;
		for (int i = 0; i < N; ++i)
		{
			if(A[i]==B[i])
			{
				amin(dp[i+1][1], dp[i][0]);
				amin(dp[i+1][1], dp[i][1]);
			}


			amin(dp[i+1][0], dp[i][0] + ( (i==0 || B[i-1]!=B[i])?1:0));
		}

		int ans = BIG;
		for (int i = 0; i <= N; ++i)
		{
			amin(ans, max(dp[i][0],rev[i]));
			amin(ans, max(dp[i][1],rev[i]));
		}

// 		for (int i = 0; i <= N; ++i)
// 		{
// 			fprintf(stderr,"%2d ",dp[i][0]);
// 		}
// 		fprintf(stderr,"\n");
// 
// 		for (int i = 0; i <= N; ++i)
// 		{
// 			fprintf(stderr,"%2d ",dp[i][1]);
// 		}
// 		fprintf(stderr,"\n");
// 
// 		for (int i = 0; i <= N; ++i)
// 		{
// 			fprintf(stderr,"%2d ",rev[i]);
// 		}
// 		fprintf(stderr,"\n");

		PRINTF("Case #%d: %d\n",testcase+1, ans);
	}

	return 0;
}
#endif