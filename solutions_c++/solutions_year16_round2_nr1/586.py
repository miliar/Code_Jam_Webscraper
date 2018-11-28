#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair<PI, PI > PII;
const double eps=1e-5;
const int inf=1e5;
const double pi=acos(-1.0);
const int N=5e5+5;

char s[2005];
int num[1005];
//vector<int> ans;
int ans[10];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%s", s);
        printf("Case #%d: ", ca++);
        int n=strlen(s);
        memset(ans, 0, sizeof(ans));
        memset(num, 0, sizeof(num));
        for(int i=0; i<n; i++)
            num[s[i]]++;

        while(num['Z']--)
        {
            num['E']--;
            num['R']--;
            num['O']--;
            ans[0]++;
        }
        while(num['G']--)
        {
            num['E']--;
            num['I']--;
            num['H']--;
            num['T']--;
            ans[8]++;
        }
        while(num['X']--)
        {
            num['S']--;
            num['I']--;
            ans[6]++;
        }
        while(num['H']--)
        {
            num['T']--;
            num['R']--;
            num['E']-=2;
            ans[3]++;
        }
        while(num['T']--)
        {
            num['W']--;
            num['O']--;
            ans[2]++;
        }
        while(num['R']--)
        {
            num['F']--;
            num['O']--;
            num['U']--;
            ans[4]++;
        }
        while(num['F']--)
        {
            num['I']--;
            num['V']--;
            num['E']--;
            ans[5]++;
        }
        while(num['V']--)
        {
            num['S']--;
            num['N']--;
            num['E']-=2;
            ans[7]++;
        }
        while(num['I']--)
        {
            num['E']--;
            num['N']-=2;
            ans[9]++;
        }
        while(num['O']--)
        {
            num['E']--;
            num['N']--;
            ans[1]++;
        }
        for(int i=0;i<10;i++)
            while(ans[i]--)
                printf("%d", i);
        puts("");
    }
    return 0;
}
/*
100
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
OZNEEORRZZERROOEEOZ
ENEEERTHSV
FISINIVEXEN
OFRU
FOUR
ISEETEEVVNRFEH
NEEEGIEHRTHOT
FVEI
ERTIENOHOZGE
WTOOTTOOEONONWTEWW
IUERVEOSXNFS
RHHTEERETE
EIFSXVI
NOWONNEONEOEETNEOO
THGEI
NOEEOTIINNEGOHENNE
NNNEVSEFIEIEV
NNFINVEENIEI
SVNEE
RIHETEFEV
FNSXSIINEVVNEEIE
TRSXVEINVUSNFOWEEEOS
OONENEEENIVNNES
THEREEHENIENTR
ZNEEROGOEOIZHERT
OERWIFTEEVXOZNIOS
FOEIVUHERIGUFTRFO
WEEREZONVITOIFN
VFIE
RUOF
ZIENOEERRTHENEON
ORTNEFOUOW
OEINSNEXO
WNRTETHEOEO
IIVIENFNSFVENEVEE
OUEFORN
NNEFROIU
EEVSEETIREHETHHEGNTR
NIVNZENIFNSREOEEOEEV
REEINOFOTOOUGWTHTW
ROZUFREO
IZHRSERFXOOTEERU
NOEREZO
HTGIE
EETONTOEHFHIUERRG
NINNNIOEEEOEENNNIN
OHNTIETEGNEEROHE
EONNSENENENEIIVN
TWTOTWWWOOWOOWOTTT
VETIEEWOOWVNFFNOTOEI
IENENORNUOF
NOENOIENENONEIENN
XIS
TSINHGVEEE
ENEONONNNEOOEOE
EIVENVNENNEEENOSS
ONE
HEOEGNEUFNREHTIITR
VEONVIIEEFNNSENE
FTESEVEHGNIIVE
VIESENXS
TWO
UREHETORF
FENOOUR
XEVFIIS
HNOFIUEORETG
TEVGINESRFHEOUORZE
EEZZRROO
UROERGNEIHOTTEHEF
TNNEOEWTWEOOOONNOE
OTOZEHEERRTW
WTTOOTTWOOWWETNOOW
NINHTIEGE
OENNIEVNESEN
HEEZTEROORIEVEFZR
ONOEOENENEOONNNEOE
EENWVETONENWOOOOSETN
ZEZRZORRZORREZEEOOEO
NNOSOXEEXIIS
ENNINNEENINEINNNNIEI
ZUFROOER
TOW
ZOER
OWT
IIENINIEONNEENENNNN
NENINOONOEEOENNE
FTRUHREEO
FONUEOR
OTEWNOOEWNOOWTETON
RVEIFSXFVONIESUE
NEOEON
ISEETFWVVENO
NSEXNNEEOINIO
OERENFOZIVREFRUOEOZ
IRXISZXOSE
TIOOEWVNEF

*/
