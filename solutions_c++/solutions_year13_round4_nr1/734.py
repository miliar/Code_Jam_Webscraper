#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <stack>
#include <utility>

#define F first
#define S second

typedef long long lnt ;
typedef std::map< lnt , lnt > mii ;
typedef mii::iterator miip ;
typedef std::pair< lnt , lnt > pii ;

const int SIZE_M = 1000 + 10 ;
const lnt MOD = 1000002013 ;
const lnt INV2 = 500001007 ;

FILE *in , *out ;

int T , n , m ;
int ent[SIZE_M] , exi[SIZE_M] , num[SIZE_M] ;

lnt ans1 , ans2 , ans3 ;

std::map< lnt , lnt > cnt ;

int na ;
lnt ary1[SIZE_M * 2] , ary2[SIZE_M * 2] ;

std::stack< pii > que ;

pii mp(lnt a , lnt b){ return std::make_pair(a , b) ;}

lnt madd(lnt a , lnt b){ return (a + b) % MOD ; }
lnt msub(lnt a , lnt b){ return ((a - b) % MOD + MOD) % MOD ; }
lnt mmul(lnt a , lnt b){ return (a * b) % MOD ; }

lnt f(lnt d)
{
	if(d == 0) return 0LL ;
	lnt t = msub(mmul(d , n) , mmul(mmul(d , d - 1) , INV2)) ;
	return t ;
}

void clear(void)
{
	cnt.clear() ;
	ans1 = ans2 = ans3 = 0 ;
	while(que.size() != 0) que.pop() ;
}

int main(void)
{
	in = fopen("A-large.in" , "r") ;
	//in = fopen("a.in" , "r") ;
	out = fopen("a.out" , "w") ;
	
	fscanf(in , "%d" , &T) ;
	for(int count = 1 ; count <= T ; ++count , clear())
	{
		printf("%d\n" , count) ;
		fscanf(in , "%d%d" , &n , &m) ;
		
		printf("%d %d\n" , n , m) ;
		
		for(int i = 1 ; i <= m ; ++i)
		{
			fscanf(in , "%d%d%d" , ent + i , exi + i , num + i) ;
			lnt d = exi[i] - ent[i] ;
			ans1 = madd(ans1 , mmul(num[i] , f(d))) ;
			if(cnt.count(ent[i]) == 0) cnt[ent[i]] = 0 ;
			if(cnt.count(exi[i]) == 0) cnt[exi[i]] = 0 ;
			cnt[ent[i]] += num[i] , cnt[exi[i]] -= num[i] ;
		}
		
		{
			int i = 0 ;
			for(miip st = cnt.begin() ; st != cnt.end() ; st++ , ++i)
				ary1[i] = (*st).F , ary2[i] = (*st).S ;
			na = i ;
		}
		
		//for(int i = 0 ; i < na ; ++i) printf("==%d %d\n" , ary1[i] , ary2[i]) ; puts("") ;
		
		for(int i = 0 ; i < na ; ++i)
		{
			if(ary2[i] > 0)
			{
				que.push(mp(ary1[i] , ary2[i])) ;
			}
			if(ary2[i] < 0)
			{
				while(ary2[i] < 0)
				{
					lnt d , s = ary1[i] - que.top().F ;
					if(que.top().S + ary2[i] >= 0)
					{
						d = -ary2[i] ;
						que.top().S -= d ;
					}
					else
					{
						d = que.top().S ;
						que.pop() ;
					}
					ans2 = madd(ans2 , mmul(d , f(s))) ;
					ary2[i] += d ;
					//printf("=%I64d\n" , ans2) ;
				}
			}
		}
		
		ans3 = msub(ans1 , ans2) ;
		fprintf(out , "Case #%d: %I64d\n" , count , ans3) ;
		//printf("%I64d %I64d\n" , ans1 , ans2) ;
	}
	
	return 0 ;
}

