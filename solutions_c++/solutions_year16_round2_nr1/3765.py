/*input
100
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
VEOEEOOOTNONTSEEWNWN
FIEV
EIONOXENNEISN
SVENE
IESEFIRIGNHXTNUO
EZERRZOO
WWTTONWOTOEOONOETW
OEUOFUFNROTRWO
ERTEH
IHNIEETNG
EINFUORN
FNINVNESEEXIIVSE
VXEINESIFNI
TIEGH
HTEER
SNEOIVEVNENEEENNS
TIFXTEHEGHEVIESIR
ETHGI
OOREEEOEZEZRNZORORZ
HEVORWEENESTT
EEXIVNERFTOEITHWSO
XSEETSEIEHTRRHIX
ENNOENONINEIOENEN
XOEERIVSFEFSUVNI
FOUR
OTWTTTOWOTTWOOWWOW
OOTWNE
SIOEXNUSEFVR
RNEXZNSIUOEXOIISRF
WOT
GTEIH
ONEESVEN
NSNNEEVFEIVONEIE
NOEONONNENOEEOWETO
ENEONIN
EVXHSSIGITNSEXIE
NXEOISENO
ONOEZRE
EONONNNOOEEEENO
IGTVOIEXESFHNIE
NSRENEEONEEVIONZFVEI
IEXWEEONINSTSVN
NTEEWOOONNOOWETTWO
OOEWIENERROOZNZTRUF
OEN
NSEENNEONEINEVNI
ENEIRNNUOOF
NESINOEENEOENVN
HESGEVITINXSE
XSIONXOSNIEE
FVITVEWTNONFEEIEWOOO
NIEN
RENTEHNEIHTERE
TOWSSIXEVEN
OOUERVFRFHIFEERTU
IFOWUURXORTFSO
IEIVSFX
IXSFVIE
SXEIZOR
GUIFNHENIREOT
GTETXHNIONEEIOOSW
RTEEH
VEEINENEVINOEFNS
FTWEINEHEGNIOIVT
IEFSVREZIXFEOEVOIN
ENXVISOIEVESNFE
ENEVS
EZOERORERZUOROFZ
ENONEOENONOEENNI
ENNNNENNENEINIOEIIN
NFEONVONEEIINE
EWWTONTOOWTOOTOWTW
UFRNEOO
INNNOOIEINENNNEENE
EOEZZOOEZRRROREEOZZR
NNNNNNENEIIIEENIENNI
TGWOIEREHZOT
NNENINIE
EONTNISENEONWVOENE
XSNVSEROINNIEUEF
EITNGHOE
ROEINNEZ
EENVOFI
EXOSREFFNUNIOROOU
NEFWEOROTZOURTHEROE
RHETHIETGE
OEOEETTNOOONNWWONE
HRETUOFRE
REZO
REUGTOIORNEHEFETH
HORFNGOIETEU
OENNNNOOOONEEENEOE
EHGIT
HRTEOEISREXZ
FRORUOZE
ZVREIWFEUEOTNVFROSEO
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
vector <ll> v;
int main() 
{
	std::ios::sync_with_stdio(false);
	ll T;
	cin>>T;
	F(t,1,T)
	{
		string s;
		cin>>s;
		ll hass[150]={0};
		ll n = s.length();
		F(i,0,n-1)
			hass[s[i]]++;
		v.clear();
		if(hass['Z']>0)
		{
			F(i,1,hass['Z'])
				v.pb(0ll);
			hass['E']-=hass['Z'];
			hass['R']-=hass['Z'];
			hass['O']-=hass['Z'];
			hass['Z']=0;
		}
		if(hass['W']>0)
		{
			F(i,1,hass['W'])
				v.pb(2ll);
			hass['T']-=hass['W'];
			hass['O']-=hass['W'];
			hass['W']=0;
		}
		if(hass['U']>0)
		{
			F(i,1,hass['U'])
				v.pb(4ll);
			hass['F'] -= hass['U'];
			hass['O'] -= hass['U'];
			hass['R'] -= hass['U'];
			hass['U']=0;
		}	
		if(hass['X']>0)
		{
			F(i,1,hass['X'])
				v.pb(6ll);
			hass['S']-=hass['X'];
			hass['I']-=hass['X'];
			hass['X']=0;
		}
		if(hass['G']>0)
		{
			F(i,1,hass['G'])
				v.pb(8ll);
			hass['E']-=hass['G'];
			hass['I']-=hass['G'];
			hass['H']-=hass['G'];
			hass['T']-=hass['G'];
			hass['G']=0;
		}
		if(hass['F'])
		{
			F(i,1,hass['F'])
				v.pb(5ll);
			hass['I'] -= hass['F'];
			hass['V'] -= hass['F'];
			hass['E'] -= hass['F'];
			hass['F'] = 0;
		}
		if(hass['O'])
		{
			F(i,1,hass['O'])
				v.pb(1ll);
			hass['N'] -= hass['O'];
			hass['E'] -= hass['O'];
			hass['O'] = 0;
		}
		if(hass['T'])
		{
			F(i,1,hass['T'])
				v.pb(3ll);
			hass['R'] -= hass['T'];
			hass['H'] -= hass['T'];
			hass['E'] -= hass['T'];
			hass['E'] -= hass['T'];
			hass['T'] = 0;
		}
		if(hass['S'])
		{
			F(i,1,hass['S'])
				v.pb(7ll);
			hass['E'] -= hass['S'];
			hass['V'] -= hass['S'];
			hass['E'] -= hass['S'];
			hass['N'] -= hass['S'];
			hass['S'] = 0;
		}
		if(hass['E'])
		{
			F(i,1,hass['E'])
				v.pb(9ll);
			hass['N'] -= hass['E'];
			hass['N'] -= hass['E'];
			hass['I'] -= hass['E'];
			hass['E'] = 0;
		}
		ll sz=v.size();
		sort(v.begin(),v.end());
		cout<<"Case #"<<t<<": ";
		F(i,0,sz-1)
			cout<<v[i];
		cout<<endl;
	}
	return 0;
}