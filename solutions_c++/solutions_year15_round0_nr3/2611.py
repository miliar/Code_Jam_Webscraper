#include <iostream>
using namespace std;

int mult(int x1, int x2) {
    int sgn = x1/4 + x2/4;
    x1 %= 4;
    x2 %= 4;
    int dig;
    if(!x1 || !x2) {
        dig = x1 + x2;
    } else if(x1 == x2) {
        dig = 4;
    }
    else {
        x1--;
        x2--;
        if(x1 == (x2 + 1) % 3) {
            sgn = 1-sgn;
        }
        dig = 4 - x1 - x2;
    }
    return (dig + sgn*4) % 8;
}

bool solve(std::string text, int x) {
    //the entire thing must have a product of -1
    int prod = 0;
    for(int i = 0; i < text.size(); i++) {
        prod = mult(prod,text[i]-'h');
    }
    if(prod == 0 || x%4 == 0) {
        return false;
    } else if(prod == 4 && x%2) { //if the product is -1 and there are odd terms
    } else if(x%2) { //if the number is odd and we have i,j,k or negative
        return false;
    }
    if(prod != 4 && (prod == 0 || x%2 )) {
        cout<<prod<<endl;
        return false;
    }

    //we also have to reach both i and j for this to be correct
    if(x > 16) {  // only need to go so far...
        x = 16;
    }
    int p1,p2,p3;
    p1 = 0;
    for(int i = 0; i < text.size()*x; i++) {
        p1 = mult(p1,text[i%text.size()]-'h');
        if(p1 == 1) {
            p2 = 0;
            for(int j = i+1; j < text.size()*x; j++) {
                p2 = mult(p2,text[j%text.size()]-'h');
                if(p2 == 2) {
                    return true; //k is guaranteed by first check
                }
            }
            return false;
        }
    }
    return false;
}


int main() {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; i++) {
        int L,X;
        cin>>L>>X;
        std::string s;
        cin>>s;
        cout<<"Case #"<<(i+1)<<": "<<(solve(s,X)?"YES":"NO")<<endl;
    }
    return 0;
}
