#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#include<string>
#include<map>
#define forn(i,n) for(int i=1;i<=n;i++)
using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");


string phone(string s){
map<char,int> a;
for(int i=0;i<s.length();i++){
    if(a.find(s[i])==a.end())a[s[i]]=1;
    else a[s[i]]++;
}
string ans="";
int b[10]={0};
while(a['Z']>0&&a['E']>0&&a['R']>0&&a['O']>0){b[0]++;
                                          a['Z']--;
                                          a['E']--;
                                          a['R']--;
                                          a['O']--;
                                          }
while(a['T']>0&&a['W']>0&&a['O']>0){b[2]++;
                                          a['T']--;
                                          a['W']--;
                                          a['O']--;
                                          }
while(a['F']>0&&a['O']>0&&a['R']>0&&a['U']>0){b[4]++;
                                          a['F']--;
                                          a['O']--;
                                          a['U']--;
                                          a['R']--;
                                          }
while(a['S']>0&&a['I']>0&&a['X']>0){b[6]++;
                                          a['S']--;
                                          a['I']--;
                                          a['X']--;
                                          }
while(a['F']>0&&a['I']>0&&a['V']>0&&a['E']>0){b[5]++;
                                          a['F']--;
                                          a['I']--;
                                          a['V']--;
                                          a['E']--;
                                          }
while(a['S']>0&&a['E']>1&&a['V']>0&&a['N']>0){b[7]++;
                                          a['S']--;
                                          a['E']-=2;
                                          a['V']--;
                                          a['N']--;
                                          }
while(a['O']>0&&a['N']>0&&a['E']>0){b[1]++;
                                          a['O']--;
                                          a['N']--;
                                          a['E']--;
                                          }

while(a['T']>0&&a['H']>0&&a['R']>0&&a['E']>1){b[3]++;
                                          a['T']--;
                                          a['H']--;
                                          a['R']--;
                                          a['E']-=2;
                                          }


while(a['E']>0&&a['I']>0&&a['G']>0&&a['H']>0&&a['T']>0){b[8]++;
                                          a['E']--;
                                          a['I']--;
                                          a['G']--;
                                          a['H']--;
                                          a['T']--;
                                          }
while(a['N']>1&&a['E']>0&&a['I']>0){b[9]++;
                                          a['N']-=2;
                                          a['I']--;
                                          a['E']--;
                                          }
while(b[0]>0){ans+="0";b[0]--;}
while(b[1]>0){ans+="1";b[1]--;}
while(b[2]>0){ans+="2";b[2]--;}
while(b[3]>0){ans+="3";b[3]--;}
while(b[4]>0){ans+="4";b[4]--;}
while(b[5]>0){ans+="5";b[5]--;}
while(b[6]>0){ans+="6";b[6]--;}
while(b[7]>0){ans+="7";b[7]--;}
while(b[8]>0){ans+="8";b[8]--;}
while(b[9]>0){ans+="9";b[9]--;}

return ans;
}
int main(){
int testcase;
fin >> testcase;
forn(i,testcase){
    string s;
    fin >> s;
    fout << "Case " << "#" << i << ": " << phone(s) << endl;
    cout << "Finish " << i << endl;
}
}
