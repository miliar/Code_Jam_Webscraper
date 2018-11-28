/** CyCraig - Google Code Jam 2015 Qualification Problem C **/
#include <iostream>
#include <string>

using namespace std;

// i=2, j=3, k=4

int map[5][5] = {
                {0,0, 0, 0, 0},
                {0,1, 2, 3, 4},
                {0,2,-1, 4,-3},
                {0,3,-4,-1, 2},
                {0,4, 3,-2,-1}
                };




void extend(string &s, int l) {
    if(l == 1) return;
    string temp = "";
    while(l--) temp += s;
    s = temp;
}

int reduce(const string s) {
    //cout << "Looking at '" << s << "'\n";
    if(s.length() < 1) return -10;
    if(s.length() == 1) {
        //cout << "Reduce '" << s << "' = " << s[0]-'i'+2 <<  "\n";        
        return (s[0]-'i'+2);
        
    }
    int x,y;
    x = s[0]-'i'+2;
    for(int i = 1; i<s.length(); i++) {
        y = s[i]-'i'+2;
        x = (x>0)?(map[x][y]):(-map[-x][y]); 
    }
    //cout << "Reduce '" << s << "' = " << x <<  "\n";
    return x;
}

string convert(int x) {
    string ret;
    if(x < 0) {
        ret = "-";
        x = -x;
    }
    ret += (x+'i'-2);
    return ret;
}

bool solve(string &str) {
    /*bool foundi = false,foundj = false,foundk = false;
    int len = str.length();
    for(int i = 0; i <= len-2 && !foundi; i++) {
        if(reduce(str.substr(0,i))==2) {
            foundi = true;
            //cout << "Found i!\n";
            for(int j = i; j <= len-1 && !foundj; j++) {
                if(reduce(str.substr(i,j))==3) {
                    //cout << "Found j!\n";
                    foundj = true;
                    for(int k = j; k <= len && !foundk; k++) {
                        if(reduce(str.substr(j+1,k))==4) {
                            //cout << "Found k!\n";
                            foundk = true;
                        }
                    }
                }
            }
            if(!foundj || !foundk) foundi = false;
        }
    }
    return (foundi && foundj && foundk);*/
    
    //return (reduce(str)==-1);
    if(reduce(str)==-1) {
        bool foundi = false,foundj = false,foundk = false;
        int len = str.length();
        for(int i = 0; i <= len-2 && !foundi; i++) {
            if(reduce(str.substr(0,i))==2) {
                foundi = true;
                //cout << "Found i!\n";
                for(int j = i; j <= len-1 && !foundj; j++) {
                    if(reduce(str.substr(i,j))==3) {
                        //cout << "Found j!\n";
                        foundj = true;
                        for(int k = j; k <= len && !foundk; k++) {
                            if(reduce(str.substr(j+1,k))==4) {
                                //cout << "Found k!\n";
                                foundk = true;
                            }
                        }
                    }
                }
                if(!foundj || !foundk) foundi = false;
            }
        }
        return (foundi && foundj && foundk);
    }
    return false;
}

int main(void) {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out", "w", stdout);
    
    int n,c=0,x,l;
    string str;
    cin >> n;
    while(n--) {
        cin >> x >> l;
        
        cin.ignore(256,'\n');
        getline(cin,str);
        //one letter cannot be reduced
        if(x==1) {
            cout << "Case #" << ++c << ": NO\n";
        }
        else {
            extend(str,l);
            
            //cannot split into three
            if(str.length() < 3) {
                cout << "Case #" << ++c << ": NO\n";
            }
            else {
                //cout << str;
                //cout << reduce(str) << '\n';
                //cout << convert(reduce(str)) << '\n';
                //cout << reduce(str);
                cout << "Case #" << ++c << ": " << ((solve(str))?"YES":"NO") << '\n';
                //cout << "Case #" << ++c << ": " << ((solve(str))?"YES":"NO") << '\n';
            }
        }
    }
    fflush(stdout);
    
    
    return 0;
}