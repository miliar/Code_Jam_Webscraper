#include<iostream>
#include<cstdio>
#include<deque>
#include<algorithm>

using namespace std;

typedef int		 			I;
typedef double	 		D;
typedef deque<D> 		QD;

#define SZ(v) 					((int)(v).size())
#define all(a) 					(a).begin(),(a).end()
#define pb						push_back
#define F(i,a,b) 				for(int i=(a);i<(b);++i)
#define R(i,n) 					F(i,0,n)
#define Fe(i,a,b)				for(int i=(a);i<=(b);++i)
#define S(x)					cin >> x


#define PLf(K) 		do {RSZ(i,K) { printf("%f ", K[i]);} printf("\n");}while(0)
#define last(A)		(*(A.end()-1))

I main() {
	I k,n; D temp;
	I c1, c2;
	QD K1,N1;
	QD K2,N2;
	S(k);
	Fe(t,1,k) {
		S(n);
		R(i,n) {S(temp); N1.pb(temp);N2.pb(temp);}
		R(i,n) {S(temp); K1.pb(temp);K2.pb(temp);}

		sort(all(K1),greater<D>()); sort(all(K2),greater<D>());
		sort(all(N1),greater<D>()); sort(all(N2),greater<D>());

		c1=0; c2=0;

		while(SZ(N1)) {
			if (N1[0]>K1[0]) {c1++; N1.pop_front(); K1.pop_back();}
			else {N1.pop_front(); K1.pop_front();}
		}

		while(SZ(N2)) {
			if(last(N2)>last(K2)) {c2++; N2.pop_back(); K2.pop_back();}
			else {N2.pop_back(); K2.pop_front();}
		}

		printf("Case #%d: %d %d\n",t,c2,c1);

		K1.clear();	K2.clear();	N1.clear();	N2.clear();
	}
}
