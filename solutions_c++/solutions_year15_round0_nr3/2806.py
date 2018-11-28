#include<cstdio>
int t,l,n,i,j,k,nr,nc,b,c,q,cc,qq,ccc,qqq,ok,n1,n2,n3,s[10100];
char tt[10100];
FILE *f,*g;
int main(){
    f=fopen("c.in","r");
    g=fopen("c.out","w");
    fscanf(f,"%d",&t);
    while(t--){
        nr=0;
        nc++;
        fscanf(f,"%d%d\n%s",&l,&n,tt);
        if(l==1){
            fprintf(g,"Case #%d: NO\n",nc);
            continue;
        }
        n1=n2=n3=0;
        for(i=1;i<=n;i++){
            for(j=0;j<l;j++){
                if(tt[j]=='i'){
                    s[++nr]=10;
                    n1++;
                }
                else if(tt[j]=='j'){
                    s[++nr]=20;
                    n2++;
                }
                else{
                    s[++nr]=30;
                    n3++;
                }
            }
        }
        if(n1>=nr-1||n2>=nr-1||n3>=nr-1){
            fprintf(g,"Case #%d: NO\n",nc);
            continue;
        }
        c=1;
        b=c;
        q=0;
        ok=0;
        for(i=1;i<=nr;i++){
             if(c==1)
                c=s[i];
            else if(c==10){
                if(s[i]==10){
                    q=(q+1)%2;
                    c=1;
                }
                else if(s[i]==20){
                    c=30;
                }
                else if(s[i]==30){
                    c=20;
                    q=(q+1)%2;
                }
            }
            else if(c==20){
                if(s[i]==10){
                    c=30;
                    q=(q+1)%2;
                }
                else if(s[i]==20){
                    q=(q+1)%2;
                    c=1;
                }
                else if(s[i]==30){
                    c=10;
                }
            }
            else if(c==30){
                if(s[i]==10){
                    c=20;
                }
                else if(s[i]==20){
                    c=10;
                    q=(q+1)%2;
                }
                else if(s[i]==30){
                    c=1;
                    q=(q+1)%2;
                }
            }
            if(c==10&&q==0){
                cc=1;
                qq=0;
                for(j=i+1;j<=nr;j++){
                    if(cc==1)
                        cc=s[j];
                    else if(cc==10){
                        if(s[j]==10){
                            qq=(qq+1)%2;
                            cc=1;
                        }
                        else if(s[j]==20){
                            cc=30;
                        }
                        else if(s[j]==30){
                            cc=20;
                            qq=(qq+1)%2;
                        }
                    }
                    else if(cc==20){
                        if(s[j]==10){
                            cc=30;
                            qq=(qq+1)%2;
                        }
                        else if(s[j]==20){
                            qq=(qq+1)%2;
                            cc=1;
                        }
                        else if(s[j]==30){
                            cc=10;
                        }
                    }
                    else if(cc==30){
                        if(s[j]==10){
                            cc=20;
                        }
                        else if(s[j]==20){
                            cc=10;
                            qq=(qq+1)%2;
                        }
                        else if(s[j]==30){
                            cc=1;
                            qq=(qq+1)%2;
                        }
                    }
                    if(cc==20&&qq==0){
                        ccc=1;
                        qqq=0;
                        for(k=j+1;k<=nr;k++){
                            if(ccc==1)
                                ccc=s[k];
                            else if(ccc==10){
                                if(s[k]==10){
                                    qqq=(qqq+1)%2;
                                    ccc=1;
                                }
                                else if(s[k]==20){
                                    ccc=30;
                                }
                                else if(s[k]==30){
                                    ccc=20;
                                    qqq=(qqq+1)%2;
                                }
                            }
                            else if(ccc==20){
                                if(s[k]==10){
                                    ccc=30;
                                    qqq=(qqq+1)%2;
                                }
                                else if(s[k]==20){
                                    qqq=(qqq+1)%2;
                                    ccc=1;
                                }
                                else if(s[k]==30){
                                    ccc=10;
                                }
                            }
                            else if(ccc==30){
                                if(s[k]==10){
                                    ccc=20;
                                }
                                else if(s[k]==20){
                                    ccc=10;
                                    qqq=(qqq+1)%2;
                                }
                                else if(s[k]==30){
                                    ccc=1;
                                    qqq=(qqq+1)%2;
                                }
                            }
                        }
                        if(ccc==30&&qqq==0){
                            ok=1;
                            break;
                        }
                    }
                    if(ok)
                        break;
                }
            }
            if(ok)
                break;
        }
        if(ok){
            fprintf(g,"Case #%d: YES\n",nc);
        }
        else
            fprintf(g,"Case #%d: NO\n",nc);
    }
    fclose(f);
    fclose(g);
    return 0;
}
