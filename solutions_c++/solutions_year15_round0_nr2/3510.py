#include<bits/stdc++.h>
using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
int d, j, mins, divide, k, maxs, mincount, cases;
cin>>cases;
for(int t=1; t<=cases; t++) {
cin>>d;
int arr[d];
maxs=0;
for(int i=0;i<d;i++)
{
	cin>>arr[i];
	if(arr[i]>maxs)
		maxs=arr[i];
}
mincount = 0;
j=1;
while(j <= maxs) {
mins = 0;
divide = 0;
k=0;
while(k < d) {
if(j >= arr[k]) {
mins = max(mins, arr[k]);
}
else {
divide = divide + arr[k]/j;
if(arr[k]%j == 0) {
divide--;// = divide - 1;
}
if(j == max(mins, j)) {
mins = j;
}
}
k++;
}
if(j==1 || (mins + divide <= mincount)) {
mincount = mins + divide;
}
j++;
}
cout<<"Case #"<<t<<": "<<mincount<<endl;
}
return 0;
}
