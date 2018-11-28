#include <iostream>
#include <unordered_set>
using namespace std;

#define lli long long int

lli countSheep(int num){
    
    lli tmp;
    int i;
    unordered_set<int> myset;
    for(i=1;;i++){
    
    tmp = i*num;
    while(tmp>0){
        int r = tmp % 10;
        myset.insert(r);
        tmp/=10;
    }    
    
    if(myset.size()==10)
    break;
        
    }
    
    return i*num;
    
}

int main() {
	// your code goes 
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin>>n;
	int c=1;
	while(n--){
	    int num;
	    cin>>num;
	    if(num == 0)
	    cout<<"Case #"<<c<<": INSOMNIA\n";
	    else
	    cout<<"Case #"<<c<<": "<<countSheep(num)<<'\n';
	    
	
	    c++;
	}
	return 0;
}
