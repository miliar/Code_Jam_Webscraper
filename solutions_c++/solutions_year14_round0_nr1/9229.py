void CDlgGoogleCodeJam::QR2014ProblemA(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, k, T, iRow1, Cards1[4][4], iRow2, Cards2[4][4], iCount, iCard;
	bool			bResult, bTest;
	CString			sReadText, sWriteText, sTempText, str;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	T = atoi(sReadText);
	for (i = 1; i <= T; i++)
	{
		// Read test
		pInputFile->ReadString(sReadText);
		sscanf_s(sReadText,"%d", &iRow1);

		for (j=0; j<4; j++)
		{
			pInputFile->ReadString(sReadText);
			sscanf_s(sReadText, " %d %d %d %d", &Cards1[j][0],  &Cards1[j][1],  &Cards1[j][2],  &Cards1[j][3]);
		}
		
		pInputFile->ReadString(sReadText);
		sscanf_s(sReadText,"%d", &iRow2);

		for (j=0; j<4; j++)
		{
			pInputFile->ReadString(sReadText);
			sscanf_s(sReadText, " %d %d %d %d", &Cards2[j][0],  &Cards2[j][1],  &Cards2[j][2],  &Cards2[j][3]);
		}

		// Do the job

		iCount = 0;
		iCard = 0;
		for (j=0; j<4; j++)
		{
			for (k=0; k<4; k++)
			{
				if (Cards1[iRow1-1][j] == Cards2[iRow2-1][k])
				{
					iCard = Cards1[iRow1-1][j];
					iCount++;
				}
				
				if (iCount > 1)
					break;
			}

			if (iCount > 1)
				break;
		}

		switch (iCount)
		{
			case 0: sTempText = "Volunteer cheated!"; break;
			case 1: sTempText.Format("%d", iCard); break;
			default: sTempText = "Bad magician!"; break;
		}
		
		// Print result
		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}
