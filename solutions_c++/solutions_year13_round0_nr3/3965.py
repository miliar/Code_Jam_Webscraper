using namespace std;
#include <iostream>
#include <string>
#include <vector>
string add(string A,string B) {
	int c=0, x=0;
    string C;
    reverse(A.begin(),A.end());
    reverse(B.begin(),B.end());
	while(x<A.size() || x<B.size()) {
		if(x<A.size()) c+=A[x]-'0';
		if(x<B.size()) c+=B[x]-'0';
		C.push_back('0'+(c%10));
		c=c/10; x++;
	}
	if(c) C.push_back('0'+c);
    reverse(C.begin(),C.end());
    return C;
}
string mul(string A,char c) {
    reverse(A.begin(),A.end());
    string C; int a=0,x;
    for(x=0;x<A.length();x++) {
        a=((A[x]-'0')*(c-'0'))+a;
        C.push_back('0'+(a%10));
        a=a/10;
    }
    while(a) {
        C.push_back('0'+(a%10));
        a=a/10;
    }
    reverse(C.begin(),C.end());
    return C;
}
bool isPal(string A) {
	int x,m=A.length()/2;
	for(x=0;x<m;x++) {
		if(A[x]!=A[A.length()-1-x]) return 0;
	}
	return 1;
}
string sq(string A) {
    string C="",B="",M; int x;
    for(x=A.length()-1;x>=0;x--) {
        M=mul(A,A[x]); M=M+B; B=B+"0";
        C=add(C,M);
    }
    return C;
}
bool Pal(long long int N) {
    int d,r=0,a=N;
    while(a) {
        d=a%10;
        r=(r*10)+d;
        a=a/10;
    }
    if(r==N) return 1;
    return 0;
}
bool hasAll(string A,char c) {
    int x;
    for(x=0;x<A.length();x++) {
        if(A[x]!=c)
            return 0;
    }
    return 1;
}
string nextPal(string A) {
    string C; int x;
    if(hasAll(A,'9')) {
        string D(A.length(),'0');
        D[0]='1'; D.push_back('1');
        return D;
    }
    int mid=A.length()/2;
    if(A.length()%2==1 && A[mid]!='9') {
        A[mid]++;
        return A;
    }
    if(A.length()%2==1 && A[mid]=='9') {
        A[mid]='0';
    }
    for(x=mid-1;x>=0;x--) {
        if(A[x]!='9') {
            A[x]++; A[A.length()-1-x]++;
            return A;
        } else {
            A[x]='0'; A[A.length()-1-x]='0';
        }
    }
}
bool isless(string A, string B) {
    if(A.length()<B.length())
        return 1;
    if(A.length()==B.length()) {
        if(A<B) return 1;
    }
    return 0;
}
int main() {
    string S,x="1",E="1";
    int y,z,C=0;
    for(y=0;y<5;y++) E=E+"0";
    vector<string> R;
    E=E+"1";
    while(1) {
        if(x==E) break;
        if(isPal(x)) {
            S=sq(x);
            if(isPal(S)) 
                R.push_back(S);
        }
        x=nextPal(x);
    }
    int T; string A,B;
    cin>>T;
    for(y=0;y<T;y++) {
        int F=0,L=0;
        cin>>A>>B;
        for(z=0;z<R.size();z++) {
            if(isless(R[z],A)) F=z+1;
            if(isless(R[z],B) || R[z]==B) L=z+1;
            else if(!(isless(R[z],A) || R[z]==A))
                break;
        }
        cout<<"Case #"<<y+1<<": "<<(L-F)<<endl;
    }
	return 0;
}
