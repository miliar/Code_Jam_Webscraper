void QR2013ProblemB(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, k, l, x, T, M, N, Lawn[100][100], iColToCheck;
	bool			bResult, bTest;
	CString		sReadText, sWriteText, sTempText, str;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	T = atoi(sReadText);
	for (i = 1; i <= T; i++)
	{
		pInputFile->ReadString(sReadText);
		sscanf(sReadText,"%d %d", &N, &M);

		// Read test
		for (j=0; j<N; j++)
		{
			pInputFile->ReadString(sReadText);
			sscanf(sReadText, " %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d"
												" %d %d %d %d %d %d %d %d %d %d", 
												&Lawn[j][0],  &Lawn[j][1],  &Lawn[j][2],  &Lawn[j][3],  &Lawn[j][4],  &Lawn[j][5],  &Lawn[j][6],  &Lawn[j][7],  &Lawn[j][8],  &Lawn[j][9], 
												&Lawn[j][10], &Lawn[j][11], &Lawn[j][12], &Lawn[j][13], &Lawn[j][14], &Lawn[j][15], &Lawn[j][16], &Lawn[j][17], &Lawn[j][18], &Lawn[j][19], 
												&Lawn[j][20], &Lawn[j][21], &Lawn[j][22], &Lawn[j][23], &Lawn[j][24], &Lawn[j][25], &Lawn[j][26], &Lawn[j][27], &Lawn[j][28], &Lawn[j][29], 
												&Lawn[j][30], &Lawn[j][31], &Lawn[j][32], &Lawn[j][33], &Lawn[j][34], &Lawn[j][35], &Lawn[j][36], &Lawn[j][37], &Lawn[j][38], &Lawn[j][39], 
												&Lawn[j][40], &Lawn[j][41], &Lawn[j][42], &Lawn[j][43], &Lawn[j][44], &Lawn[j][45], &Lawn[j][46], &Lawn[j][47], &Lawn[j][48], &Lawn[j][49], 
												&Lawn[j][50], &Lawn[j][51], &Lawn[j][52], &Lawn[j][53], &Lawn[j][54], &Lawn[j][55], &Lawn[j][56], &Lawn[j][57], &Lawn[j][58], &Lawn[j][59], 
												&Lawn[j][60], &Lawn[j][61], &Lawn[j][62], &Lawn[j][63], &Lawn[j][64], &Lawn[j][65], &Lawn[j][66], &Lawn[j][67], &Lawn[j][68], &Lawn[j][69], 
												&Lawn[j][70], &Lawn[j][71], &Lawn[j][72], &Lawn[j][73], &Lawn[j][74], &Lawn[j][75], &Lawn[j][76], &Lawn[j][77], &Lawn[j][78], &Lawn[j][79], 
												&Lawn[j][80], &Lawn[j][81], &Lawn[j][82], &Lawn[j][83], &Lawn[j][84], &Lawn[j][85], &Lawn[j][86], &Lawn[j][87], &Lawn[j][88], &Lawn[j][89], 
												&Lawn[j][90], &Lawn[j][91], &Lawn[j][92], &Lawn[j][93], &Lawn[j][94], &Lawn[j][95], &Lawn[j][96], &Lawn[j][97], &Lawn[j][98], &Lawn[j][99]
					);
		}

		// Do the job

		bResult = true;
		for (j=0; j<N; j++)
		{
			for (k=0; k<M; k++)
			{
				for (l=0; l<M; l++)
				{
					if (Lawn[j][k] > Lawn[j][l])
					{
						for (x = 0; x<N; x++)
						{
							if (Lawn[j][l] < Lawn[x][l])
							{
								bResult = false;
								break;
							}
						}
					}

					if (!bResult)
						break;
				}

				if (!bResult)
					break;
			}

			if (!bResult)
				break;
		}

		if (bResult)
			sTempText = "YES";
		else
			sTempText = "NO";

		// Print result
		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}
