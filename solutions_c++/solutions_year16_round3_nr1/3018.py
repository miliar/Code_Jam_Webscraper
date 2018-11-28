#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
#define loop(i,a,b) for(i=a;i<b;i++)
#define ll long long int 
int main() {
              ll n,i,t,j,k,l,s,c,m=0,flag;
              cin>>t;
              while(t!=0){
                  cin>>n;
                  //flag=0;
                  m++;
                  s=0;
                  ll a[n];
                  loop(i,0,n){
                      cin>>a[i];
                      s+=a[i];
                  }
                  cout<<"Case #"<<m<<": ";
                  if(n==2){
                           if(a[0]==a[1]){
                               while(a[0]--){
                                   printf("AB ");
                               }
                           }
                  else{
                      if(a[0]>a[1]){
                          while(a[0]!=a[1]){
                              cout<<"A ";
                              a[0]--;
                          }
                          while(a[0]--){
                              cout<<"AB ";
                          }
                      }
                      else{
                          while(a[1]!=a[0]){
                              cout<<"B ";
                              a[1]--;
                          }
                          while(a[0]--){
                              cout<<"AB ";
                          }
                      }
                  }
                  }
                  if(n==3){
                    if(a[0]==a[1] && a[1]==a[2]){
                        s=s/3;
                        if(s==1){
                            cout<<"A BC";
                        }
                        if(s==2){
                            cout<<"AA BC BC";
                        }
                        if(s==3){
                            cout<<"AA BC BC A BC";
                        }
                    }
                    else if((a[0]==a[1] && a[1]!=a[2]) || (a[1]==a[2] && a[2]!=a[0]) || (a[0]==a[2] && a[2]!=a[1])){
                        if(a[0]==a[1]){
                            while(a[2]--){
                                printf("%c ",(char)(2+65));
                            }
                            while(a[0]--){
                               printf("%c%c ",(char)(0+65),(char)(1+65)); 
                            }
                        }
                        else if(a[0]==a[2]){
                            while(a[1]--){
                                printf("%c ",(char)(1+65));
                            }
                            while(a[0]--){
                               printf("%c%c ",(char)(0+65),(char)(2+65)); 
                            }
                        }
                        else if(a[2]==a[1]){
                            while(a[0]--){
                                printf("%c ",(char)(0+65));
                            }
                            while(a[1]--){
                               printf("%c%c ",(char)(1+65),(char)(2+65)); 
                            }
                        }
                    }
                  else{
                      while(s!=0){
                      flag=0;
                      l=s-2;
                      if(l%2==0){
                          flag=0;
                      }
                      k=l/2;
                      c=0;
                          if(flag==1){
                              loop(i,0,n){
                          if(a[i]>=k){
                             c++;
                          }
                      }
                          }
                          else if(flag==0){
                      loop(i,0,n){
                          if(a[i]>k){
                             c++;
                          }
                      }
                          }
                   if(c==1){
                       if(flag==1){
                       loop(i,0,n){
                           if(a[i]>=k){
                               printf("%c%c ",(char)(i+65),(char)(i+65));
                               a[i]-=2;
                               s-=2;
                               c=0;
                               break;
                           }
                       }
                       }
                       else if(flag==0){
                         loop(i,0,n){
                           if(a[i]>k){
                               printf("%c%c ",(char)(i+65),(char)(i+65));
                               a[i]-=2;
                               s-=2;
                               c=0;
                               break;
                           }
                       }  
                       }
                   }
                          if(c==2){
                              if(flag==1){
                              loop(i,0,n){
                                  if(a[i]>=k){
                                      printf("%c",(char)(i+65));
                                      a[i]--;
                                  }
                              }
                              }
                              else if(flag==0){
                                 loop(i,0,n){
                                  if(a[i]>k){
                                      printf("%c",(char)(i+65));
                                      a[i]--;
                                  }
                              } 
                              }
                              cout<<" ";
                              s-=2;
                          }
                          
                        if(a[0]==a[1] && a[1]==a[2]){
                        s=s/3;
                        if(s==1){
                            cout<<"A BC";
                        }
                        if(s==2){
                            cout<<"AA BC BC";
                        }
                        if(s==3){
                            cout<<"AA BC BC A BC";
                        }
                            s=0;
                    }
                          
                  }
                  }
              }
                  cout<<endl;
                  t--;
              }
  return 0;
}
