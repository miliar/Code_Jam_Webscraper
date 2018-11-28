#include<stdio.h>
#include<stdlib.h>

//#define DEBUG

enum val {
    pi=0, // i
    pj=1, // j
    pk=2, // k
    p1=3, // 1
    ni=4, // -i
    nj=5, // -j
    nk=6, // -k
    n1=7  // -1
};

bool is_neg(val a) {
    return a==ni || a==nj || a==nk || a==n1;
}

val abs(val a) {
    switch(a) {
    case ni: return pi;
    case nj: return pj;
    case nk: return pk;
    case n1: return p1;
    default: return a;
    }
}

val neg(val a) {
    switch(a) {
    case pi: return ni;
    case pj: return nj;
    case pk: return nk;
    case p1: return n1;
    case ni: return pi;
    case nj: return pj;
    case nk: return pk;
    case n1: return p1;
    default: throw "1234";
    }
}

val mul(val a, val b) {
    //return calmap[((int)a)*7+((int)b)];
    val ca=abs(a);
    val cb=abs(b);
    val res;
    if(ca==p1) res=cb;  // 1*x=x
    else if(cb==p1) res=ca; // x*1=x
    else if(ca==cb) res=n1; // x*x=-1 (x!=1)
    else if(ca==pi && cb==pj) res=pk;
    else if(ca==pi && cb==pk) res=nj;
    else if(ca==pj && cb==pi) res=nk;
    else if(ca==pj && cb==pk) res=pi;
    else if(ca==pk && cb==pi) res=pj;
    else if(ca==pk && cb==pj) res=ni;
    else throw "123";
    if( (is_neg(a) == is_neg(b))) {  // if -a and -b or a and b
        return res;
    } else {    // a or b is negative
        return neg(res);
    }
}

/** calucalte in^p */
val pow(val in, int p) {
    if(in==p1) return p1;   // always 1
    if(in==n1) return (p&1)?n1:p1;  // -1 * -1 = 1
    if((p&1)==0) return n1;     // always -1 - x*x or x*x*x*x or x*x*x*x*x*x
    return in;  // always else its input - x or x*x *x or x*x*x*x *x
}

void print(val v) {
    switch(v){
    case pi: printf("i"); break;
    case pj: printf("j"); break;
    case pk: printf("k"); break;
    case p1: printf("1"); break;
    case ni: printf("-i"); break;
    case nj: printf("-j"); break;
    case nk: printf("-k"); break;
    case n1: printf("-1"); break;
    }
}

val to_val(char v) {
    switch(v) {
    case 'i': return pi;
    case 'j': return pj;
    case 'k': return pk;
    }
    throw "1234";
}

int main(int argc, char** argv) {
    int t;
    char txt[10002];
    val in[10002];

    scanf("%d",&t);
    for(int ti=0;ti<t;++ti) {
        int l,x;
        // read inpu
        scanf("%d %d",&l,&x);
        scanf("%s",txt);

        bool res;
        if(l*x>=3) { // there should be at least 3 input chars
#ifdef DEBUG
            printf("Input: ");
#endif
            for(int i=0;i<l;++i) {
                in[i]=to_val(txt[i]); // convert from char to enum format
#ifdef DEBUG
                print(in[i]);
#endif
            }
            val totalone=p1;
#ifdef DEBUG
            printf("\nSum parts: p1");
#endif

            for(int i=0;i<l;++i) {  // calc total value
                totalone=mul(totalone,in[i]);
#ifdef DEBUG
                printf("*");
                print(in[i]);
                printf("=");
                print(totalone);
                printf(", ");
#endif
            }
            //val total=pow(totalone,x);
            val total=p1;
            for(int i=0;i<l*x;++i) {  // calc total value
                total=mul(total,in[i%l]);
            }

#ifdef DEBUG
            val totaltmp=p1;
            if(x<10) printf("\nSum parts: p1");
            for(int i=0;i<l*x;++i) {  // calc total value
                totaltmp=mul(totaltmp,in[i%l]);
                if(x<10) {
                    printf("*");
                    print(in[i%l]);
                    printf("=");
                    print(totaltmp);
                    printf(", ");
                }
            }
            printf("\nTotal tmp sum: ");
            print(totaltmp);
#endif
#ifdef DEBUG
            printf("\nTotal one sum: ");
            print(totalone);
            printf(" Total: ");
            print(total);
            printf("\n");
#endif
            if(total!=n1) { // total sum has to be 1

                res=false;      // if not then it cannot be right
            } else {    // if total sum is 1 then
                int limit=x>5?5*l:x*l;
                int prefix_len=-1;
                // find smallest prefix that gives i
                val tmp=p1;
#ifdef DEBUG
                printf("Prefix sum: p1");
#endif
                for(int i=0;i<limit;++i) {
                    tmp=mul(tmp,in[i%l]);
#ifdef DEBUG
                    printf("*");
                    print(in[i%l]);
                    printf("=");
                    print(tmp);
                    printf(", ");
#endif
                    if(tmp==pi) {
                        prefix_len=i+1;
                        break;
                    }
                }
#ifdef DEBUG
                printf("\nPrefix len: %d\n",prefix_len);
                printf("Suffix sum: p1");
#endif
                // find smallest suffix that gives k
                int suffix_len=-1;
                tmp=p1;
                for(int i=0;i<limit;++i) {
                    tmp=mul(in[l-(i%l)-1],tmp);
#ifdef DEBUG
                    printf("*");
                    print(in[l-(i%l)-1]);
                    printf("=");
                    print(tmp);
                    printf(", ");
#endif
                    if(tmp==pk) {
                        suffix_len=i+1;
                        break;
                    }
                }
#ifdef DEBUG
                printf("\nSuffix len: %d\n",suffix_len);
#endif
                res=false;
                if(prefix_len!=-1 && suffix_len!=-1) {
                    if(prefix_len + suffix_len<x*l) {
                        res=true;
                    }
                }
            }
        } else {
            res=false;
        }

        printf("Case #%d: %s\n",ti+1, res?"YES":"NO");
    }

    return 0;
}
