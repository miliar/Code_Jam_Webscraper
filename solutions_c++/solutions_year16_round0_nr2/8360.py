/*
 *	Revenge of the Pancakes - Versão 1.0
 *	Desenvolvido por: Nelson Carvalho de Morais Junior
 *	Email: nelson.carvalho1303@gmail.com
 *	Data: 09-04-2016
 *	Local: Cotia, São Paulo, Brasil
 */
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
// Protótipos de função
void Inverte (char str[100], int qtde);
int VerificaSmile (char str[100]);
int main () {
	// Arquivos entrada/saída
	FILE *fileInput;
	FILE *fileOutput;
	// Declaração de variáveis
	int T;					// Entrada - Iterações
	char S[1000];			// Entrada - String +/-
	int F;					// Saída - Flip
	int a, b;				// Contadores
	int fSmile, fContinua;	// Flags
	// Leitura de arquivos
	fileInput = fopen ("B-large.in", "r");
	fileOutput = fopen ("B-large.out", "w");
	// Obter iterações
	fscanf (fileInput, "%d", &T);
	for (a = 0; a < T; a ++) {
		fscanf (fileInput, "%s", S);
		// Zerar quantidade de Flip
		F = 0;
		// Verificar Smile
		fSmile = VerificaSmile (S);
		while (fSmile == 0) {
			// Zerar flag Continua e contador b
			fContinua = 1;
			b = 1;
			// Obter intervalos de valores repetidos da string S
			while (fContinua == 1) {
				if (S[0] == S[b]) {
					b ++;
				} else {
					fContinua = 0;		
				}
			}
			Inverte (S, b);
			// Incrementar Flips
			F ++;
			fSmile = VerificaSmile (S);
		}
		fprintf (fileOutput, "Case #%d: %d\n", a + 1, F);
	}
	return 0;
}
// Função para inverter panquecas
void Inverte (char str[100], int qtde) {
	// Variáveis contador e auxiliar
	int i, aux;
	aux = 1;
	// Obter o período repetido de +/- e inverter o sinal para -/+
	for (i = 0; i < qtde; i ++) {
		if (str[i] == '+') {
			str[i] = '-';
		} else {
			str[i] = '+';
		}
	}
}
// Função para verificar se os rostos das panquecas estão para cima ou para baixo
int VerificaSmile (char str[100]) {
	int i;
	// Verificar todos os valores da string, se achar algum valor -, retorna 0 para continuar os Flips
	for (i = 0; i < 100; i ++) {
		if (str[i] == '-') {
			return 0;
		}
	}
	return 1;
}
