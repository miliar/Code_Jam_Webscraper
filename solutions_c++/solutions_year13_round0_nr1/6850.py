#include<fstream>
using namespace std;
ifstream f("Input");
ofstream g("Output");
int i,t,j,k,nr,p;
char a[5][5];
int main()
{ f>>t;
  for(i=1;i<=t;++i) { for(j=1;j<=4;++j) for(k=1;k<=4;++k) f>>a[j][k];
                      p=1;
                      nr=0;
                      j=1;
                      k=1;
					  while(a[j][k]=='X'||a[j][k]=='T'&&k<=4) { ++nr;
																++k;
															   }
					  if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					  if(p) { nr=0;
					          k=1;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          k=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          k=2;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          k=3;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          k=4;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4) { ++nr;
					                                                    ++j;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4&&k>=1) { ++nr;
					                                                          ++j;
					                                                          --k;
																			 }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          k=4;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4&&k>=1) { ++nr;
					                                                          ++j;
					                                                          --k;
					                                                         }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
							  j=1;
					          k=1;
					          while(a[j][k]=='X'||a[j][k]=='T'&&j<=4&&k<=4) { ++nr;
					                                                          ++j;
					                                                          ++k;
					                                                         }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=1;
					          k=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&j<=4&&k<=4) { ++nr;
					                                                          ++j;
					                                                          ++k;
					                                                         }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=2;
					          k=1;
					          while(a[j][k]=='X'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
                              if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
							  k=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=3;
					          k=1;
							  while(a[j][k]=='X'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          k=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
					          j=4;
					          k=1;
					          while(a[j][k]=='X'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"X won"<<'\n',p=0;
					         }
					  if(p) { nr=0;
							  k=1;
					          while(a[j][k]=='O'||a[j][k]=='T'&&k<=4) { ++nr;
					                                                    ++k;
					                                                   }
					          if(nr==4) g<<"Case #"<<i<<": "<<"O won"<<'\n',p=0;
					         }
					  if(p) { for(j=1;j<=4;++j) for(k=1;k<=4;++k) if(a[j][k]=='.') { p=0;
																					 j=5;
																					 k=5;
																					}
							  if(!p) g<<"Case #"<<i<<": Game has not completed"<<'\n';
					         }
					  if(p) g<<"Case #"<<i<<": Draw"<<'\n';
                     }
  return 0;
}
