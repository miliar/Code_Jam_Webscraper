#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int count1=0;
string p;
void flip( int n) { string z=p;
                         for(int i=0;i<n+1;i++)
                         {  p[i]=z[n-i];
                            if(p[i]=='+')
                               p[i]='-';
                            else
                                p[i]='+';
                         }
                         count1++;

                        }
void trick( int n){               if(n==-1)
                                   return;
                               else{  if(p[n]=='+') { return trick(n-1);
                                            }
                              else { if(p[n]=='-' &&  p[0]=='-')
                                        {flip(n);
                                       return trick(n-1);}
                                      else {   int k=n;
                                            while(1){   if(p[k]=='-')
                                                            k--;
                                                         else
                                                            break;
                                                         }
                                              flip(k);
                                              return trick(n);

                                               }

                                    }

                               }

                                    }

int main(){  ifstream in("input.in");
               ofstream out("output.in");

               int t,a;
                in>>t;
                for(a=1;a<t+1;a++) { in>>p;
                                  int l = p.length();
                                 trick(l-1);
                                  out<<"Case #"<<a<<": "<<count1<<endl;
                                  count1=0;
                                  }

           return 0;

           }
