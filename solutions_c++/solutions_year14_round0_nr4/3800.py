#include <cstdio>
#include <algorithm>
using namespace std;

void make() {
	int n;
	int winW=0;
	int winD=0;
	scanf("%d",&n);
	float Naomi[n], Ken[n];
	for (int i=0;i<n;i++) {
		scanf("%f",&Naomi[i]);
	}
	for (int i=0;i<n;i++) {
		scanf("%f",&Ken[i]);
	}
	
	sort(Ken,Ken+n);
	sort(Naomi,Naomi+n);
	
	int k=0;
	for (int i=0;i<n;++i) {
		for (int j=k;j<n;j++) {
			if (Naomi[i]<Ken[j]) {winW++;k=j+1;break;}
		}
	}
	
	winW=n-winW;
	k=0;
	for (int i=0;i<n;i++) {
		if (Naomi[i]<Ken[k]) {winD++;}
		else {k++;}
	}
	winD=n-winD;		

    printf("%d %d\n",winD,winW);
    return;
}

int main() {
	int counter = 0;
    int t; scanf("%d", &t);
    while(t--) {
		printf("Case #%d: ", ++counter);
        make();
    }
    return 0;
}
