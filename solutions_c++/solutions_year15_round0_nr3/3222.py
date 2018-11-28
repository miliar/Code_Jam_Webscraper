#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
using namespace std;


int matriz[4][4];
string cts(char c){
    stringstream ss;
    ss << c;
    return ss.str();
}
int conversor_LetraANum(string letra)
{
	if(letra.size() ==2)
	{
		letra = letra.at(1);
	}
	if(letra=="1")
	{
		return 1;
	}
	if(letra=="i")
	{
		return 2;
	}
	if(letra=="j")
	{
		return 3;
	}
	if(letra=="k")
	{
		return 4;
	}
}
string conversor_NumaLet(int num)
{
	if(num ==1)
	{
		return "1";
	}
	if(num ==2)
	{
		return "i";
	}
	if(num ==3)
	{
		return "j";
	}
	if(num ==4)
	{
		return "k";
	}
	if(num ==-1)
	{
		return "-1";
	}
	if(num ==-2)
	{
		return "-i";
	}
	if(num ==-3)
	{
		return "-j";
	}
	if(num ==-4)
	{
		return "-k";
	}
}
string multiplicar(string fila,string columna)
{
	//Verifico si tiene signo para poder descartarlo despues
	//Convierto la letra en numeros para poder buscar en la matriz
	//Lo mando a un conversor de numeros a letras
	//Agrego o no el signo dependiendo de si tiene o no
	//Retorno el resultado
	bool tiene_signo = false;
	if((fila.at(0) == '-' && columna.at(0)!='-') || (fila.at(0) != '-' && columna.at(0)=='-'))
	{
		tiene_signo = true;
		if(fila.at(0)=='-')
		{
			fila = fila.at(1);
		}
		else
		{
			columna = columna.at(1);
		}
	}
	
	int num_fila = conversor_LetraANum(fila);
	int num_columna = conversor_LetraANum(columna);
	int valor = matriz[num_fila-1][num_columna-1];
	string valor_letra = conversor_NumaLet(valor);

	if(tiene_signo)
	{
		if(valor_letra.size()==2)
		{
			valor_letra = valor_letra[1];
		}
		else
		{
			valor_letra = "-" + valor_letra;
		}
	}

	return valor_letra;

}


int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int cantidad_casos;
	cin>> cantidad_casos;

	//Matriz dada

	
	// mat[0] = 1  mat[1] = i mat[2] = j mat[3] = k
	// en la matriz 0=1 1=i 2=j 3=k
	matriz[0][0] = 1;
	matriz[0][1] = 2;
	matriz[0][2] = 3;
	matriz[0][3] = 4;
	matriz[1][0] = 2;
	matriz[1][1] = -1;
	matriz[1][2] = 4;
	matriz[1][3] = -3;
	matriz[2][0] = 3;
	matriz[2][1] = -4;
	matriz[2][2] = -1;
	matriz[2][3] = 2;
	matriz[3][0] = 4;
	matriz[3][1] = 3;
	matriz[3][2] = -2;
	matriz[3][3] = -1;


	
	for(int i = 1;i<=cantidad_casos;i++)
	{
		int cantidad_letras;
		cin>> cantidad_letras;
		int cantidad_repeticiones;
		cin>> cantidad_repeticiones;
		string palabra;
		cin>>palabra;
		string palabra_completa = palabra;
		if(cantidad_repeticiones > 1)
		{
			for(int x =2;x<=cantidad_repeticiones;x++)
			{
				palabra_completa = palabra_completa + palabra;
			}
			
		}
		bool i_encontrada = false;
		int caso_i_encontrada=0;
		int caso_i_actual_encontrada=0;
		bool j_encontrada = false;
		int caso_j_encontrada=0;
		int caso_j_actual_encontrada=0;
		bool k_encontrada = false;
		int proxima_letra = 0;
		string letra_actual;
		bool primera_j = true;
		bool primera_k = true;
		bool Ya_incorrecto = false;
		if(palabra_completa.size()<3)
		{
			cout << "Case #" << i << ": " << "No" << endl; 
			Ya_incorrecto = true;
		}
		else
		{
			for(int s = 1;s<palabra_completa.size();s++)
			{
				if(s == 1)
				{
					letra_actual = multiplicar(cts(palabra_completa[s-1]),cts(palabra_completa[s]));
				}
				else
				{
					letra_actual = multiplicar(letra_actual,cts(palabra_completa[s]));
				}
			}
		}
		if(letra_actual == "-1")
		{
			while(!i_encontrada || !j_encontrada || !k_encontrada){
				proxima_letra = 0;
				i_encontrada =false;
				j_encontrada = false;
				primera_j = true;
				primera_k = true;
				while((i_encontrada==false || caso_i_actual_encontrada<=caso_i_encontrada))
				{
				
					if(proxima_letra ==0)
					{
						if(palabra_completa[0] == 'i')
						{
							caso_i_actual_encontrada++;
							i_encontrada = true;
							proxima_letra++;
					
						}
				
						else
						{
							if(proxima_letra+2 > palabra_completa.size())
							{
								break;
							
							}
							else
							{
								letra_actual = multiplicar(cts(palabra_completa[0]),cts(palabra_completa[1]));
					
								proxima_letra = 2;
						
								if(letra_actual == "i")
								{
									caso_i_actual_encontrada ++;
									i_encontrada=true;
								
								}
							}
						}
					}
					else
					{
						if(proxima_letra==palabra_completa.size())
						{
							break;
						}
						else
						{
							letra_actual = multiplicar(letra_actual,cts(palabra_completa[proxima_letra]));
							
							if(letra_actual=="i")
							{
								i_encontrada = true;
								caso_i_actual_encontrada++;
						
							}
							proxima_letra++;

						}
					}
				}
				if(proxima_letra+2 > palabra_completa.size())
				{
					break;
							
				}
				caso_i_encontrada = caso_i_actual_encontrada;
				caso_i_actual_encontrada = 0;
				while(j_encontrada ==false || caso_j_actual_encontrada<=caso_j_encontrada)
				{
					if(primera_j)
					{
						if(palabra_completa[proxima_letra] == 'j')
						{
							caso_j_actual_encontrada++;
							j_encontrada = true;
							proxima_letra++;
					
						}
						else
						{
							if(proxima_letra+2 > palabra_completa.size())
							{
								break;
							}
							else
							{
								letra_actual = multiplicar(cts(palabra_completa[proxima_letra]),cts(palabra_completa[proxima_letra+1]));
					
								proxima_letra +=2;
						
								if(letra_actual == "j")
								{
									caso_j_actual_encontrada ++;
									j_encontrada=true;
								
								}
							}
						}
						primera_j = false;
					}
					else
					{
						if(proxima_letra==palabra_completa.size())
						{
							break;
						}
						else
						{
							letra_actual = multiplicar(letra_actual,cts(palabra_completa[proxima_letra]));
						
							if(letra_actual=="j")
							{
								j_encontrada = true;
								caso_j_actual_encontrada++;
							
							}
							proxima_letra++;

						}
					}
				}
				if(proxima_letra+1 > palabra_completa.size())
				{
					break;
							
				}
				caso_j_encontrada = caso_j_actual_encontrada;
				caso_j_actual_encontrada = 0;
			while(k_encontrada == false || palabra_completa.size()!=proxima_letra)
				{
				if(primera_k)
				{
					primera_k = false;
					if(palabra_completa[proxima_letra] == 'k' && palabra_completa.size()==proxima_letra+1 )
					{
					
						k_encontrada = true;
						proxima_letra++;
					
					}
					else
					{
						if(proxima_letra+2 > palabra_completa.size())
						{
							break;
						}
						else
						{
							letra_actual = multiplicar(cts(palabra_completa[proxima_letra]),cts(palabra_completa[proxima_letra+1]));
					
							proxima_letra +=2;
						
							if(letra_actual == "k" && palabra_completa.size()==proxima_letra)
							{
						
								k_encontrada=true;
						
							}
						}
					}
				
				}
				else
				{
					if(proxima_letra==palabra_completa.size())
					{
						break;
					}
					else
					{
						letra_actual = multiplicar(letra_actual,cts(palabra_completa[proxima_letra]));
					
						if(letra_actual=="k" && palabra_completa.size()==proxima_letra+1)
						{
							k_encontrada = true;
					
						
						}
					
						proxima_letra++;
					
					}
				}
			}
			if(proxima_letra+2 > palabra_completa.size())
			{
				break;
							
			}
		
		
		
		}
	}
	else
	{
		if(Ya_incorrecto == false)
		{
			Ya_incorrecto=true;
			cout << "Case #" << i << ": " << "No" << endl; 
		
		}
	}
	if(i_encontrada && j_encontrada && k_encontrada)
	{
		cout << "Case #" << i << ": " << "Yes" << endl;
	}
	else
	{
		if(Ya_incorrecto == false)
		{
			Ya_incorrecto=true;
			cout << "Case #" << i << ": " << "No" << endl; 
			
		}
	}
}
}