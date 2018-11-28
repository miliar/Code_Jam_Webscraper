#include <iostream>
#include <math.h>
using namespace std;

typedef long long ll;

const int lim = 1e7;
int ch = 0, a[40];

bool Palindrom(ll chislo)
{
    ll mas[20];
 
    ll i(0), count;
    while(chislo > 0)
    {
        mas[i] = chislo%10;
        chislo /=10;
        ++i;
    }
    count = i;
    for(i = 0; i < count / 2; ++i)
        if(mas[i] != mas[count - 1 - i])
            break;
 
    return (i == count/2) ? true : false;
}

void generation(){
	for(ll i = 1; i < lim; i++){
			if(Palindrom(i)){
				if((Palindrom(i * i))){
					a[ch] = i * i;
					ch++;
				}
			}
		}
}

int bust(int m, int n){
	int d = 0;
	for(int i = 0; i < 39; i++){
		if(a[i] >= m && a[i] <= n){
			d++;
		}
	}
	return d;
}

int main(){
	freopen("test.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	generation();

	int k, m, n;
	scanf("%d", &k);
	for(int i = 0; i < k; i++){
		scanf("%d %d", &m, &n);
		printf("Case #%d: %d\n", i + 1, bust(m, n));
	}
}