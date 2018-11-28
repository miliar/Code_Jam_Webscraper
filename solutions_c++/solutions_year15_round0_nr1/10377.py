#include<cstdio>
#include<iostream>
#include<vector>

using namespace std;

int main(){
	int i, n, m, j, k;
	int ans = 0;
	int freecount = 0;
	int extra = 0;
	string s;
	cin >> n;
	i=0;
	while(i<n){
		cin >> m >> s;
		int *a = new int[m+1];
		freecount = 0;
		extra = 0;
		j = 0;
		while(j<=m)
		{
			a[j] = s[j]-'0';
			j++;
		}
		freecount = a[0]; 
		for(j=1;j<=m;j++)
		{
			if(a[j]>0)
			{
				k = a[j];
				while(k>0){
					if(freecount>=j)
					{
						freecount++;	
					}
					else{
						extra += (j-freecount);
						freecount += extra+1;
					}
					k--;	
					//cout << "Loop: " << freecount << " " << extra << endl;
				}
			}
			//cout << freecount << " " << extra << endl;
		}
		cout << "Case #" << (i+1) << ": " << extra << endl;
		i++;
	}	

	return 0;
}
