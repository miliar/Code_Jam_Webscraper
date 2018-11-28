#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("in_jam.txt","r",stdin);
	//freopen("out_jam1.txt","w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int t = 0;t < T;t++){
		scanf("%d",&N);
		float a[N],b[N];
		for(int j = 0;j < N;j++){
			cin >> a[j];
			//scanf("%lf",&a[j]);
		}
		for(int j = 0;j < N;j++){
			cin >> b[j];
			//scanf("%lf",&b[j]);
		}
		// cout << "Started : " ;
		// for(int i = 0;i < N;i++){
		// 	cout << a[i] << endl;
		// }
		// cout << "Finished";
		sort(a,a + N);
		sort(b,b + N);
		// cout << "Started : " ;
		// for(int i = 0;i < N;i++){
		// 	cout << a[i] << endl;
		// }
		// cout << "Finished";
		int count1 = 0,count2 = 0,i = N - 1,j = N - 1;
        while (i>=0 && j>=0){
            if(a[i]>b[j]){
                count1=count1+1;
                i = i - 1;
                j = j - 1;
            }
            else{
                j = j - 1;
            }
        }
        j = N - 1;
        i = N - 1;
        while (i>=0 and j>=0){
            if(b[j] > a[i]){
                count2 = count2 + 1;
                i = i - 1;
                j = j - 1;
            }
            else {
                i = i - 1;
            }
        }
		printf("Case #%d: %d %d \n",t + 1,count1,N - count2);
	}
	return 0;
}
