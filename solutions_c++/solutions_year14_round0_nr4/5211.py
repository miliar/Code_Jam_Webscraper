#include<iostream>
#include<algorithm>
#include<utility>

using namespace std;

bool sort_bool(pair<double,char> p1, pair<double,char> p2){
if(p1.first <= p2.first)
return true;
return false;

}

int main() {
ios_base::sync_with_stdio(false);
int num_Test;
pair<double,char> arr[2001];
int num_Blocks;
cin >> num_Test;
int i,j=0;
double temp;
while(num_Test--) {
j++;
cin >> num_Blocks;
for(i=0;i<num_Blocks;i++){
cin >> temp;
arr[i]=make_pair(temp,'n');
}
for(i=0;i<num_Blocks;i++){
cin >> temp;
arr[i+num_Blocks]=make_pair(temp,'k');
}
int opt=0, deceit=0;
int opt_count=0, deceit_count=0;
sort(arr,arr+num_Blocks*2,sort_bool);
for(i=0;i<num_Blocks*2;i++){
if(arr[i].second == 'n')
opt_count++;
else if(arr[i].second == 'k' && opt_count > 0){
opt_count --;
opt ++;
}
if(arr[i].second == 'k')
deceit_count ++;
else if(arr[i].second == 'n' && deceit_count > 0){
deceit_count --;
deceit ++;
}
}
opt = num_Blocks - opt;
cout << "Case #" << j << ": " << deceit << " " << opt << '\n';
}

return 0;
}
