#include <iostream>
#include <string>
using namespace std;
int rec(bool* s,int n, int cont, int t){
	// cout<<"entrada: "<<endl;
	// for (int i = 0; i < t; ++i)
	// 	cout<<(s[i]?"+":"-");
	// cout<<endl;
	int u=n-1;
	bool flag=false;
	//encontramos el ultimo que está volteado
	for (int i=n-1;i>=0;--i)
		if( !s[i] ){
			u=i;
			flag=true;
			break;
		}
	//si no hay entonces terminamos
	if ( not flag){
		// cout<<"Está correcto"<<endl;
		return cont;
	}
	n=u+1; //solo nos interesan  hasta donde esta el primer error
	//si hay, entonces tenemos que asegurar que antes de voltear los primeros 0..n-1
	//los primeros esten volteados tambien, aprovechamos esto para dejar al final tantos 
	//como sea posible

	// cout<<"nos importa del 0 al "<<u<<endl;

	//si el primero esta bien, volteamos tantos como es posible
	if( s[0]){
		// cout<<"El primero está bien, debemos voltear ";
		int u=0;
		for(int i=0;i<n;++i)
			if( !s[i] ){//encontramos el primero al revez
				u=i-1; 
				break;
			}
		// cout<<"los primeros 0.."<<u<<endl;
		cont++;
		bool aux;
		int i,f;
		i=0;
		f=u;
		while(i<=f){
			aux=s[i];
			s[i]=!s[f];
			if(i!=f)
				s[f]=!aux;
			++i;
			--f;
		}
		//luego volteamos todo
		// cout<<"luego volteamos todo"<<endl;
		cont++;  
		i=0;
		f=n-1;
		while(i<=f){
			aux=s[i];
			s[i]=!s[f];
			if(i!=f)
				s[f]=!aux;
			++i;
			--f;
		}
		//al menos los ultimos u estan bien ahora
		return rec(s,n-u,cont,t);
	}else{
		// cout<<"el primero esta volteado, damos toda la vuelta"<<endl;
		//si el primero esta volteado entonces podemos proceder
		bool aux; 
		int i,f;
		i=0;
		f=n-1;
		while(i<=f){
			aux=s[i];
			s[i]=!s[f];
			if(i!=f)
				s[f]=!aux;
			++i;
			--f;
		}
		cont++;
		// cout<<"luego llamamos recursivamente"<<endl;
		return rec(s,n-1,cont,t);//sabemos que al menos dejamos uno bien
	}
}
int f(string s){ 
	int n=s.size();
	bool* a=new bool(n);
	for (int i = 0; i < n; ++i)
		a[i]=s[i]=='+';
	int res= rec(a,n,0,n);
	delete[] a;
	return res;
}
int  main(int argc, char const *argv[])
{
	int T;
	cin>>T;
	string s;
	for (int i = 0; i < T; ++i)
	{
		cin>>s;
		// cout<<s<<endl;
		cout<<"Case #"<<i+1<<": "<<f(s)<<"\n";
		// cout<<endl;
		// if (i>6)
		// 	break;
	}
	return 0;
}